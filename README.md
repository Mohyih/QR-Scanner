# QR Generator and Scanner App

This project is a simple QR code generator and scanner system built using Python. It allows you to:
- Generate QR codes from structured JSON data
- Scan QR codes using a camera
- Automatically store and display scanned QR code data in a local JSON file
- View and search scanned records through a simple GUI application

Features

- Generates scannable QR codes from custom JSON
- Detects QR codes via webcam and decodes them
- Stores scanned data with timestamps
- GUI interface with search, filter, and login

Requirements

- Python 3.x
- Required libraries:
    pip install opencv-python pyzbar customtkinter

How to Run

1. Generate a QR Code -  python generate_qr.py
2. Scan the QR Code - python qr_scanner.py
3. View the Scanned Data from the QR Code - python viewer_app.py

Default Login (GUI)

    Username: admin
    Password: admin

- The current scanner source is set to **webcam**, but this system can also be adapted for use with an **ESP32-CAM** 
- Make sure your webcam is working before running `qr_scanner.py`.
- Scanned QR data must be in valid **JSON format** for it to be decoded and stored correctly.

Sample QR Code JSON for creating QR Code Data in data.json
{
  "identifier": "QR001",
  "content": "Romyliza Boado",
  "scanDate": "2025-03-10",
  "source": "Webcam",
  "validity": true
}

Created for educational purposes.

