import xml.etree.ElementTree as ET
import mysql.connector

# ==========================================
# 1. DATABASE CONNECTION SETUP
# ==========================================
try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="Network_Security_DB"
    )

    cursor = conn.cursor()
    print("Database Connected Successfully")
    print("Connection Status: True\n")

except mysql.connector.Error as err:
    print(f"Database Connection Failed: {err}")
    exit()


# ==========================================
# 2. PARSE XML FILE
# ==========================================
try:
    tree = ET.parse("scan_result.xml")
    root = tree.getroot()

except Exception as e:
    print(f"XML File Error: {e}")
    conn.close()
    exit()


print("Nmap Scan Results")
print("-" * 30)


# ==========================================
# 3. READ HOSTS AND INSERT DATA
# ==========================================

for host in root.findall("host"):

    address = host.find("address")

    if address is not None:

        ip_addr = address.attrib["addr"]

        print("IP Address:", ip_addr)


        # Insert Device
        cursor.execute(
            "INSERT INTO Scanned_Devices (IP_Address) VALUES (%s)",
            (ip_addr,)
        )

        conn.commit()

        device_id = cursor.lastrowid

        print("Device ID:", device_id)


        # Read Ports
        ports = host.find("ports")

        if ports is not None:

            for port in ports.findall("port"):

                port_number = port.attrib["portid"]
                protocol = port.attrib["protocol"]


                state = port.find("state")
                service = port.find("service")


                if state is not None:

                    port_state = state.attrib["state"]


                    if service is not None:
                        service_name = service.attrib.get("name", "Unknown")
                    else:
                        service_name = "Unknown"


                    print("Port:", port_number)
                    print("Protocol:", protocol)
                    print("State:", port_state)
                    print("Service:", service_name)


                    # Insert Open Ports
                    cursor.execute(
                        """
                        INSERT INTO Open_Ports
                        (Device_ID, Port_Number, Service_Name, Port_State)
                        VALUES (%s,%s,%s,%s)
                        """,
                        (
                            device_id,
                            port_number,
                            service_name,
                            port_state
                        )
                    )

                    conn.commit()

                    print("Port Data Inserted")
                    print("-" * 30)



# ==========================================
# 4. CLOSE DATABASE
# ==========================================

cursor.close()
conn.close()

print("Database Connection Closed")
