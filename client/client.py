import time
import requests

while True:
	try:
		response = requests.get("http://web:8098")
		print(f"Web status: {response.status_code}, text: {response.text}", flush=True)
	except Exception as e:
		print(f"Error: {e}", flush=True)
	time.sleep(5)
