# Google IT Automation with Python

> **A practical automation portfolio combining Python, Linux, process management, regular expressions, and VLSI engineering workflows.**

This repository contains my hands-on work while learning **Google IT Automation with Python**, with the exercises adapted toward practical engineering and **VLSI RTL verification** use cases.

The goal is not only to learn Python syntax, but to understand how Python can be used as an **automation layer around engineering tools and workflows**.

---

## 🎯 Repository Objective

The repository focuses on developing automation skills that can be applied to real engineering environments.

The central workflow is:

```text
Python
   │
   ├── Execute external tools
   ├── Monitor processes
   ├── Capture output
   ├── Parse logs
   ├── Detect failures
   └── Generate useful results
```

These concepts are demonstrated using examples related to **RTL compilation, simulation, and verification log analysis**.

---

## 🛠️ Technologies & Tools

| Technology / Tool | Purpose                               |
| ----------------- | ------------------------------------- |
| Python 3          | Automation and scripting              |
| `subprocess`      | External process execution            |
| `re`              | Regular expression and log processing |
| SystemVerilog     | RTL and verification testbenches      |
| Icarus Verilog    | RTL compilation                       |
| VVP               | Simulation execution                  |
| Linux             | Development environment               |
| Git               | Version control                       |
| GitHub            | Portfolio and project hosting         |

---

# 📚 Learning Progress

## Day 01 — Managing Data & Processes

**Status: ✅ Completed**

The first module focuses on controlling processes, capturing command output, and extracting useful information from engineering logs.

### Completed Topics

* [x] Python Subprocess Fundamentals
* [x] `subprocess.run()`
* [x] `subprocess.Popen()`
* [x] Process return codes
* [x] `stdout` and `stderr`
* [x] `capture_output=True`
* [x] `text=True`
* [x] `check=True`
* [x] `communicate()`
* [x] Exception handling
* [x] Process timeout handling
* [x] Regular Expressions
* [x] Log filtering
* [x] PASS / FAIL extraction
* [x] Verification log analysis
* [x] VLSI-oriented automation

---

# 🔬 Day 01 — VLSI Automation Workflow

The concepts were implemented around a simple RTL verification workflow.

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
          ┌─────────┼─────────┐
          ▼         ▼         ▼
         PASS      FAIL     WARNING
                    │
                    ▼
              Failure Report
```

This demonstrates how Python can be used to automate repetitive tasks that would otherwise require manually executing multiple Linux and EDA commands.

---

# 📁 Repository Structure

```text
Google_IT_Automation/
│
├── Day-01_Managing_Data_Processes/
│   │
│   ├── 01_subprocess_basics/
│   │   ├── rtl/
│   │   │   └── and_gate.sv
│   │   │
│   │   ├── tb/
│   │   │   └── and_gate_tb.sv
│   │   │
│   │   └── scripts/
│   │       ├── compile.py
│   │       ├── popen.py
│   │       └── timeout.py
│   │
│   ├── 04_regex_log_filtering/
│   │   ├── logs/
│   │   │   └── simulation.log
│   │   │
│   │   └── scripts/
│   │       ├── read_logs.py
│   │       └── task_analyzer.py
│   │
│   └── README.md
│
├── .gitignore
└── README.md
```

The repository intentionally contains only completed work and relevant source/input files. Generated binaries, waveform files, Python cache files, and temporary artifacts are excluded through `.gitignore`.

---

# ⚙️ Engineering Concepts Practiced

## 1. External Process Automation

Python was used to control external command-line tools.

Example workflow:

```text
Python
  │
  ▼
Icarus Verilog
  │
  ▼
Compiled RTL
  │
  ▼
VVP
  │
  ▼
Simulation Output
```

This establishes the basic pattern of using Python as an automation wrapper around engineering tools.

---

## 2. Process Management

Both `subprocess.run()` and `subprocess.Popen()` were explored.

### `subprocess.run()`

Used for straightforward synchronous execution:

```text
Execute
   ↓
Wait
   ↓
Collect Result
```

### `subprocess.Popen()`

Used when greater control over the running process is required:

```text
Start Process
      ↓
Maintain Process Handle
      ↓
Monitor / Communicate
      ↓
Collect Result
```

This distinction becomes useful for longer-running simulations and regression environments.

---

## 3. Output & Error Handling

The automation scripts work with:

```text
stdout
stderr
returncode
```

This allows a Python script to distinguish between:

* Normal tool output
* Warnings
* Errors
* Successful execution
* Failed execution

Exception handling was also practiced using:

```python
subprocess.CalledProcessError
subprocess.TimeoutExpired
```

---

## 4. Regular Expression Log Processing

Regular expressions were used to extract structured information from simulation logs.

Example:

```text
[19:42:07] FAIL: TEST_004 - expected y=0, observed y=x
```

The log can be transformed into:

```text
19:42:07 | TEST_004 | expected y=0, observed y=x
```

This demonstrates how unstructured tool output can be converted into information suitable for automated analysis.

---

## 5. Verification Log Analysis

The log-analysis workflow identifies verification results such as:

```text
PASS
FAIL
WARNING
ERROR
INFO
```

Example summary:

```text
PASS    : 4
FAIL    : 2
WARNING : 4
ERROR   : 5
INFO    : 13
```

Failed tests can also be extracted with their timestamps, test identifiers, and failure reasons.

---

# 🧠 Automation Pattern

The core engineering pattern developed during Day 01 is:

```text
        EXECUTE
           │
           ▼
        CAPTURE
           │
           ▼
          PARSE
           │
           ▼
         ANALYZE
           │
           ▼
         REPORT
```

This pattern can be extended to larger engineering automation systems.

---

# 🚀 Future Direction

The next stages of this repository will progressively extend Python automation toward larger engineering workflows.

Potential applications include:

* Automated RTL compilation
* Batch simulation
* RTL regression testing
* Test-result collection
* Failure extraction
* Regression summaries
* EDA tool automation
* Verification report generation
* CI/CD-based verification workflows

The long-term objective is to develop automation skills that complement **RTL Design and Functional Verification** work.

---

# 📈 Progress

| Area                           | Status         |
| ------------------------------ | -------------- |
| Python Automation              | 🟢 In Progress |
| Linux Automation               | 🟢 In Progress |
| Subprocess Management          | ✅ Completed    |
| Process Output Handling        | ✅ Completed    |
| Regular Expressions            | ✅ Completed    |
| Log Processing                 | ✅ Completed    |
| Verification Log Analysis      | ✅ Completed    |
| VLSI-oriented Automation       | ✅ Completed    |
| Larger RTL Automation Workflow | 🔜 Next        |

---

# 👨‍💻 Author

**Prashik Wankhede**

**Focus:**
Python Automation · VLSI · RTL Design · Functional Verification · Linux

**Repository:**
`Google_IT_Automation`

---

> **Learning principle:** Automate repetitive work, make failures visible, and turn raw tool output into useful engineering information.
