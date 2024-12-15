# FPGA Module: Data Processor

This folder contains the Verilog code for the FPGA processing logic.

## Steps to Compile and Load the FPGA Design

1. Open Quartus Prime and create a new project.
2. Add `data_processor.v` to the project.
3. Configure the HPS-to-FPGA interface using Platform Designer (AXI).
4. Generate the `.sof` bitstream file.
5. Load the `.sof` file onto the FPGA using Quartus Programmer.

## Functionality

- The `data_processor` module receives a 32-bit input value from the HPS.
- It doubles the input value and sends it back to the HPS.

