import requests
import schedule
import time
import sys

def upload_xml_to_api(xml_file_path, api_url, sheet_id):
    try:
        with open(xml_file_path, 'rb') as file:
            files = {'score_sheet': file}
            data = {'sheet_id': sheet_id}
            response = requests.post(api_url, files=files, data=data)
            if response.status_code == 200:
                print("XML file uploaded successfully to the API 🚀")
            else:
                print(f"Failed to upload XML file. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {e}")

def job(xml_file_path, sheet_id):
    api_url = "http://localhost:8383/api/pm/v1/uplink/scoresheet" 
    upload_xml_to_api(xml_file_path, api_url, sheet_id)

def ask_for_sheet_id():
    while True:
        sheet_id = input("Please enter the card ID: ")
        if sheet_id.strip():  # Check if input is not empty
            return sheet_id
        else:
            print("🔴 Card ID cannot be empty.")

def ask_for_file_path():
    while True:
        file_path = input("Please enter the file path of the XML file: ")
        if file_path.strip():  # Check if input is not empty
            return file_path
        else:
            print("🔴 File path cannot be empty.")

def loading_animation(seconds):
    for i in range(seconds):
        sys.stdout.write('\rWaiting' + '.' * (i % 3) + ' ' * 3)
        sys.stdout.flush()
        time.sleep(1)

sheet_id = ask_for_sheet_id()
print("Sheet ID saved:", sheet_id)
file_path = ask_for_file_path()
print("File path saved:", file_path)

# Schedule the job to run every minute
schedule.every(1).minutes.do(job, file_path, sheet_id)

while True:
    schedule.run_pending()
    loading_animation(60)  # Waiting animation for 60 seconds
