import requests
from requests.structures import CaseInsensitiveDict
import sys, time
import json

# Settings
ratelimit=2 # seconds of delay between request
filename = 'data.json'
max_fails = 5 # maximum number of fails before quitting
startidx = 1350 # start and end id to request
endidx = 1514

# Get Cookie and token from chrome.
headers=CaseInsensitiveDict()
headers = {
    "Accept": "application/json, text/plain, */*",
    "Cookie": "remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d=eyJpdiI6ImVNVGw1K2tNUWFZUW03eUpOdVhjQ1E9PSIsInZhbHVlIjoiMSsrTkRjZ3hpZWVCM0hBVmsrUUphVUw4VW9QbUVISmVmZzArZjRKSmdhMmhmY0I3Y1dINmVad1RGYm96Z3dsNVI1OTQ5ME1GdlRKR1lmdnQ3TjVSbmlXaHNRZUpraHA5RUNpb0JmMFwvV09jPSIsIm1hYyI6IjhlNWIwMmYwZWU5YzVlYzVlMGE2ZDEyMWE2NjVlODMxOTYxOTM3MDg5ZDBiN2VjYWIwY2RjMDdhNTRjNmQxMzEifQ%3D%3D; _gid=GA1.2.1452602476.1696003114; _ga_TWG41QRWLZ=GS1.1.1696003113.5.1.1696004015.0.0.0; _ga=GA1.2.551594005.1688468596;", # From chrome...
    "Connection": "keep-alive",
    "Referer": "https://essentialoils.org/db",
    "token": "eyJpdiI6IllubVFpR2ZHa1Y5WEs3dk8zXC9GNjNRPT0iLCJ2YWx1ZSI6IlwvTkNHaTZybkFSMnlEaEh5R0RwbGw4UWZjZVwvbHBMVStveFlVTnZ5RFcwMG9SNnczcCt6S0xuSDY1RUFPK3phd3dcL1h0WUNaRllDYlBhZENISU5hZFJ3PT0iLCJtYWMiOiJhZGI2MmQyNzFhZjMwYWM4ODE5NDkxNDk1YThlZTljY2U5OWRlNGUzNjViNDRkNzI3N2U2ZDU4MmEyZWM4NTEwIn0%3D", # From chrome...
    "X-Requested-With": "XMLHttpRequest",
}
def write_to_file(filename, data):
    listObj = []

    # Try appending, if no file exist. 
    try:
        with open(filename) as fp:
            listObj = json.load(fp)
            listObj.append(data)
    except:
        listObj.append(data)

    with open(filename, 'w+') as json_file:
        json.dump(listObj, json_file, 
                            indent=4,  
                            separators=(',',': '))
    

# The API endpoint to communicate with
base_url_post = "https://essentialoils.org/db"
latest = time.time()

# Set start index and lists for storing response
response_list = []
last_write_id = startidx

for id in range(startidx, endidx):
    # add a time delay between requests
    while (time.time()-latest)<ratelimit:
        time.sleep(0.01) 
    
    # i is number to append to base_url_post
    url_post = base_url_post+str(id)
    # Status printout
    print(f"Getting data for id: {id}, time:{time.time()-latest}")
    # A POST request to the API
    latest = time.time()
    post_response = requests.get(url_post, headers=headers)
    
    # Skip incorrect responses
    if post_response.status_code != 200:
        max_fails = max_fails-1
        print(f"Id: {id}, Status code:{post_response.status_code}. \
            Something went wrong.")
        if max_fails<=0:
            sys.exit()
        continue 
    
    # Store response in a list
    response_list.append(post_response.json())

    # Write to file every N:th response
    if id-last_write_id >= 499 or id==endidx-1:
        write_to_file(filename, response_list) 
        last_write_id = id
        response_list = []