#!/usr/bin/env python3

import subprocess

try:
    # Step 1: Compile RTL + Testbench
    result = subprocess.run(
        [
            "iverilog",
            "-g2012",
            "-o",
            "../build/and_gate.out",
            "../rtl/and_gate.sv",
            "../tb/and_gate_tb.sv"
        ],
        check=True,
        capture_output=True,
        text=True
    )

    print("Compilation successful.")
    print("Compile return code:", result.returncode)

    # Step 2: Start simulation using Popen()
    process = subprocess.Popen(
        [
            "vvp",
            "../build/and_gate.out"
        ],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    # Step 3: Wait for simulation and collect output
    stdout, stderr = process.communicate()

    print("\nSimulation output:")
    print(stdout)

    print("Simulation return code:", process.returncode)

    if stderr:
        print("Simulation errors:")
        print(stderr)

except subprocess.CalledProcessError as e:
    print("Compilation failed.")
    print("Return code:", e.returncode)
    print("Compiler error:")
    print(e.stderr)