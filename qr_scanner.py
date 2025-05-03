import cv2
from pyzbar.pyzbar import decode
import json
from datetime import datetime
import os

seen_ids = set()

if not os.path.exists("scanned_data.json"):
    with open("scanned_data.json", mode='w') as json_file:
        json.dump([], json_file) 

with open("scanned_data.json", mode='r+') as json_file:
    json_data = json.load(json_file) 

    cap = cv2.VideoCapture(0)
    print("Scanning for QR codes. Press 'q' to quit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        decoded_objs = decode(frame)
        for obj in decoded_objs:
            try:
                qr_data_str = obj.data.decode('utf-8')

                qr_data = json.loads(qr_data_str)
                identifier = qr_data.get("identifier")
                
                if identifier and identifier not in seen_ids:
                    seen_ids.add(identifier)
                    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    
                    json_entry = {
                        "identifier": identifier,
                        "content": qr_data.get("content", ""),
                        "scanDate": qr_data.get("scanDate", ""),
                        "source": qr_data.get("source", ""),
                        "validity": qr_data.get("validity", ""),
                        "detectedAt": timestamp
                    }

                    json_data.append(json_entry)
                    
                    json_file.seek(0)  
                    json.dump(json_data, json_file, indent=4)  
                    print(f"Scanned and stored in JSON: {identifier}")

            except Exception as e:
                print(f"Error reading QR data: {e}")
                print("Non-JSON QR or error reading QR")

        cv2.imshow("QR Scanner", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
