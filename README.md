# fpga-trader

This repository demonstrates a simple workflow for making API calls with the HPS on a DE10-Nano and processing the data on the FPGA.

## Project Structure

- `hps/api_call.py`: Python script to fetch data from an API and write to FPGA.
- `fpga/data_processor.v`: Verilog module to process incoming data from the HPS.

## Prerequisites

- Python 3.x with `requests` library
- Quartus Prime Lite Edition
- DE10-Nano Development Kit with Linux installed on the HPS
