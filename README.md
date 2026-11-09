# Vectorized Growth Matrix

> A high-efficiency computational tool that leverages NumPy array broadcasting and meshgrid coordinate expansion to generate multidimensional investment compounding matrices without explicit Python iteration loops.

---

## Overview

Financial modeling tools often suffer from performance degradation and verbose iteration logic when calculating compound interest projections across expansive multi-variable parameter spaces (varying interest rates and time horizons). Traditional nested `for` loops introduce interpreter overhead and complicate vector arithmetic. `vectorized-growth-matrix` solves this friction by utilizing C-optimized array broadcasting, mapping initial principal values across multi-dimensional coordinate grids to compute long-term compounding balances instantly in a single vectorized operation.

---

## How It Works

The execution pipeline operates through three distinct stages:

1. **Terminal Boundary Validation:** Before any calculation occurs, helper functions intercept terminal inputs (`get_float_input`, `get_int_input`) to ensure principal amounts, interest rates, and time horizons strictly satisfy domain constraints, causing malformed entries to fail fast with clear prompts.
2. **Coordinate Grid Generation:** Validated rate vectors and time sequences are transformed into 2D coordinate arrays using `np.meshgrid`.
3. **Vectorized Compounding Engine:** The compounding formula $A = P(1 + r)^t$ is evaluated across contiguous memory blocks using `np.power`, eliminating Python-level loop overhead and leveraging CPU cache efficiency before formatting the output into a structured `pandas.DataFrame`.

---

## Key Features

* **Zero-Loop Vectorization:** Computes expansive matrix projections entirely through NumPy array broadcasting.
* **Rigorous Terminal Validation:** Safeguards against invalid float and integer entries with robust error handling loops.
* **Localized Tabular Formatting:** Automatically aligns matrix rows (years) and columns (interest rates) while formatting values into localized Indian Rupee (`₹`) representations.
* **Zero External State:** Operates as a stateless execution script without requiring database persistence or external configuration files.

---

## Tech Stack & Core Dependencies Breakdown

* **Python 3.10+:** Core runtime leveraging modern type hinting structures and standard library constructs.
* **NumPy:** Provides C-contiguous array allocation, coordinate meshgrids, and vectorized exponentiation primitives.
* **Pandas:** Structures multidimensional numerical outputs into indexed DataFrames with axis labeling for analytical clarity.

---

## Environment & Web-Based Quick Start

You can run and test this repository directly inside your browser via GitHub Codespaces or a standard Python virtual environment.

### 1. Virtual Environment Setup
Clone or open the repository in your workspace, then initialize your environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

### 2. Execution
Run the script directly from your terminal or Codespace:
```bash
python main.py
```

## Repository Structure
```bash
vectorized-growth-matrix/
├── .github/
│   └── workflows/
│       └── ci.yml
├── .gitignore
├── README.md
├── main.py
└── requirements.txt
```

## Roadmap

**[ ] Type Stubs & Strict Typing:** Introduce .pyi type stubs and run MyPy in strict mode to enforce rigorous static type safety across array dimensions.

**[ ] Data Export Pipeline:** Add support for exporting generated growth matrices directly to CSV and Excel spreadsheet formats.

**[ ] Structural Logging:** Integrate structured logging handlers to track execution performance metrics and parameter ranges.