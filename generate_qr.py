import qrcode
import json
import os

with open("data.json", "r") as file:
    data_list = json.load(file)

os.makedirs("output_qr", exist_ok=True)

for entry in data_list:
    qr = qrcode.make(json.dumps(entry))
    filename = f"output_qr/{entry['identifier']}.png"
    qr.save(filename)
    print(f"QR saved: {filename}")
