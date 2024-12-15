import requests
import mmap
import struct

def fetch_data():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": "bitcoin", "vs_currencies": "usd"}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()
        return int(data['bitcoin']['usd'] * 100)  # Convert to cents for fixed-point processing
    else:
        print(f"Error: {response.status_code}")
        return None

def write_to_fpga(data):
    # Map FPGA memory region (replace 0xC0000000 with your FPGA base address)
    with open("/dev/mem", "r+b") as f:
        mem = mmap.mmap(f.fileno(), 0x1000, offset=0xC0000000)
        mem.write(struct.pack('I', data))  # Write integer data
        mem.close()

data = fetch_data()
if data:
    print(f"Fetched Data: {data}")
    write_to_fpga(data)

