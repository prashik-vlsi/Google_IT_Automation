# Day 01 — Managing Data & Processes with Python

> **Google IT Automation with Python — Practical Engineering Portfolio**

This module focuses on using Python to automate system-level tasks, execute external tools, capture process output, and transform unstructured log data into actionable verification information.

The practical exercises are implemented around a **VLSI RTL verification workflow**, connecting Python automation with SystemVerilog, Icarus Verilog, simulation, and log analysis.

---

## Overview

The objective of this module was to move beyond basic Python scripting and use Python as an **automation layer around engineering tools**.

The workflow developed during this module:

```text
SystemVerilog RTL
       │
       ▼
Python Automation
       │
       ├── Compile RTL
       │
       ├── Execute Simulation
       │
       ├── Capture stdout / stderr
       │
       └── Analyze Verification Logs
                    │
                    ▼
             Structured Results
                    │
                    ├── PASS
                    ├── FAIL
                    ├── WARNING
                    └── ERROR
```

---

## Technologies & Tools

| Technology     | Purpose                               |
| -------------- | ------------------------------------- |
| Python 3       | Automation and log processing         |
| `subprocess`   | External process execution            |
| `re`           | Regular expression based log analysis |
| SystemVerilog  | RTL and verification testbench        |
| Icarus Verilog | RTL compilation                       |
| VVP            | Simulation execution                  |
| Linux          | Development environment               |
| Git / GitHub   | Version control and portfolio         |

---

# 1. Python Subprocess Automation

The first part of the module focused on controlling external processes from Python.

### Concepts Implemented

* `subprocess.run()`
* `subprocess.Popen()`
* `capture_output=True`
* `text=True`
* `check=True`
* Process return codes
* `stdout`
* `stderr`
* `communicate()`
* `CalledProcessError`
* `TimeoutExpired`

### VLSI Application

Python was used to automate an RTL compilation and simulation flow instead of manually executing every command.

Example workflow:

```text
and_gate.sv
     │
     ▼
Icarus Verilog
     │
     ▼
and_gate.out
     │
     ▼
VVP Simulation
     │
     ▼
Simulation Output
```

This demonstrates how Python can act as an automation wrapper around EDA tools.

---

# 2. Capturing Process Output

The automation scripts capture both standard output and standard error from external processes.

This allows the script to distinguish between:

```text
Successful execution
       │
       ├── stdout → normal tool output
       │
       └── stderr → warnings/errors/diagnostics
```

The process return code is also checked to determine whether execution completed successfully.

---

# 3. Advanced Subprocess Management

`subprocess.Popen()` was used when more control over a running process was required.

Compared with `subprocess.run()`:

```text
subprocess.run()
    → execute
    → wait
    → collect result
```

while:

```text
subprocess.Popen()
    → start process
    → maintain process handle
    → communicate with process
    → monitor completion
```

This distinction is particularly relevant to long-running simulation and regression workflows.

---

# 4. Regular Expression Based Log Processing

The second major part of the module focused on processing VLSI-style simulation logs.

Python's `re` module was used to identify:

* `INFO`
* `WARNING`
* `ERROR`
* `PASS`
* `FAIL`

### Example Log Entry

```text
[19:42:07] FAIL: TEST_004 - expected y=0, observed y=x
```

A regular expression was used to extract structured information:

```python
r"\[(\d+:\d+:\d+)\]\s+FAIL:\s+(TEST_\d+)\s+-\s+(.*)"
```

The capture groups provide:

```text
group(1) → timestamp
group(2) → test ID
group(3) → failure reason
```

Result:

```text
19:42:07 | TEST_004 | expected y=0, observed y=x
```

---

# 5. Verification Log Analysis

The log analyzer was developed to produce a summary of the verification run.

Example result:

```text
PASS    : 4
FAIL    : 2
WARNING : 4
ERROR   : 5
INFO    : 13
```

Failed tests can additionally be extracted with their timestamp and failure reason.

This converts an unstructured simulation log into information that can be consumed by engineers or further automation.

---

# 6. Repository Structure

```text
Day-01_Managing_Data_Processes/
│
├── 01_subprocess_basics/
│   ├── rtl/
│   ├── tb/
│   └── scripts/
│
├── 02_capturing_output/
│
├── 03_advanced_subprocess/
│
├── 04_regex_log_filtering/
│   ├── logs/
│   ├── scripts/
│   └── tb/
│
├── 05_log_analysis/
│
├── 06_mini_project/
│
├── data/
├── notes/
└── README.md
```

Generated build artifacts and temporary files are excluded through `.gitignore`.

---

# 7. Key Engineering Takeaways

### Process Automation

Python can control existing engineering tools instead of replacing them.

### Error Handling

Return codes, `stdout`, and `stderr` provide programmatic ways to detect and diagnose failures.

### Log Processing

Regular expressions can transform unstructured tool output into structured information.

### Verification Automation

The same approach can be extended from a single RTL simulation to larger regression environments.

### Automation Pipeline

The overall engineering pattern is:

```text
Execute
   ↓
Capture
   ↓
Parse
   ↓
Analyze
   ↓
Report
```

---

# 8. Practical Outcome

By completing this module, the workflow progressed from manually running individual commands to building a Python-controlled verification flow:

```text
                 Python Automation
                       │
          ┌────────────┼────────────┐
          ▼            ▼            ▼
       Compile      Simulate       Logs
          │            │            │
          └────────────┼────────────┘
                       ▼
                 Log Analysis
                       │
                       ▼
              Verification Report
```

This provides a foundation for future automation involving:

* RTL regression testing
* Automated compilation
* Batch simulation
* Test result collection
* Failure extraction
* Regression summaries
* EDA tool automation
* CI/CD integration for verification workflows

---

## Status

**Day 01 — Completed**

| Area                           | Status |
| ------------------------------ | ------ |
| Python subprocess fundamentals | ✅      |
| External command execution     | ✅      |
| Output and error capture       | ✅      |
| Advanced process management    | ✅      |
| Regular expressions            | ✅      |
| Log filtering                  | ✅      |
| Log analysis                   | ✅      |
| VLSI-oriented automation       | ✅      |

---

## Next Step

The next stage is to combine these concepts into a larger **automated RTL verification workflow**, where Python can execute simulations, analyze regression logs, detect failures, and generate verification reports automatically.

---

**Author:** Prashik Wankhede
**Domain:** Python Automation · VLSI · RTL Verification · Linux
**Repository:** `Google_IT_Automation`
