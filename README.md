# Nmap XML Parser v1.1

A Python-based Nmap XML Parser that analyzes Nmap XML scan reports and stores network scan information into a MariaDB relational database.

## Project Overview

This project automates the process of reading Nmap XML output files and extracting important network information such as:

- IP Addresses
- Open Ports
- Port States
- Running Services

The extracted information is stored in a structured relational database for analysis.

## Project Workflow

Nmap Scan → XML Report → Python Parser → MariaDB Database

## Features

- Parses Nmap XML scan reports using Python
- Extracts host IP addresses
- Extracts port numbers and services
- Stores scanned devices in database
- Stores open ports with service details
- Uses relational database design with foreign key relationships
- Provides structured security scan data storage

## Technologies Used

- Python
- XML Parsing
- Nmap
- MariaDB / MySQL
- Kali Linux
- Git & GitHub

## Database Structure

### Scanned_Devices Table

Stores discovered devices:

- Device_ID
- IP_Address

### Open_Ports Table

Stores port information:

- Port_ID
- Device_ID
- Port_Number
- Service_Name
- Port_State

The Device_ID creates a relationship between scanned devices and their open ports.

## Installation & Usage

1. Run an Nmap scan and generate XML output:
nmap -oX scan_result.xml target_ip


2. Run the Python parser:


python3 parser.py


3. The scan results will be stored in the MariaDB database.

## Skills Demonstrated

- Python Programming
- Network Scanning
- XML Data Processing
- Database Integration
- SQL Queries
- Linux Environment
- Cybersecurity Fundamentals

## Author

Saif Ali
