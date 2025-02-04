import requests
import json

# Define the URL for inserting a new note
url = 'https://rag.bolt-m3kz.workers.dev/notes'

# Open the file and read it line by line
file_path = r'C:\Users\dm\Desktop\a.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Headers as provided in the curl command
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:135.0) Gecko/20100101 Firefox/135.0",
    "Accept": "*/*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "HX-Request": "true",
    "HX-Current-URL": "https://rag.bolt-m3kz.workers.dev/write",
    "Content-Type": "application/json",
    "Origin": "https://rag.bolt-m3kz.workers.dev",
    "Alt-Used": "rag.bolt-m3kz.workers.dev",
    "Connection": "keep-alive",
    "Referer": "https://rag.bolt-m3kz.workers.dev/write",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Priority": "u=0",
    "TE": "trailers"
}

# Loop over the lines and insert them as individual notes
for line in lines:
    note_data = {
        "text": line.strip()  # Use .strip() to remove any leading/trailing whitespace
    }

    # Make a POST request to insert the note with headers and JSON data
    response = requests.post(url, headers=headers, json=note_data)

    # Check if the request was successful
    if response.status_code == 200:
        print(f"Successfully inserted note: {line.strip()}")
    else:
        print(f'Failed to insert note. Status code: {response.status_code}')
