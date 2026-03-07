import requests

files = {
    "scan_t1": open("test1.png", "rb"),
    "scan_t2": open("test2.png", "rb")
}

response = requests.post(
    "http://127.0.0.1:5001/compare",
    files=files
)

print(response.json())
