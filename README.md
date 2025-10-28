# IS601 Midterm Project — Enhanced Calculator (Python)

### Author: Ishan Rehan  
**Course:** IS601 — Python for Web API Development  
**Institution:** New Jersey Institute of Technology (NJIT)

---

## Overview
An enhanced command-line calculator demonstrating OOP, design patterns, automated testing, and CI/CD.  
Implements Factory, Memento, and Observer patterns with undo/redo, logging, and autosave.  
Includes color-coded CLI output and 96% unit test coverage verified by GitHub Actions.

---

## Features
- Arithmetic: add, subtract, multiply, divide, power, root, modulus, int_divide, percent, abs_diff  
- Undo/Redo using Memento pattern  
- Auto-save & logging via Observer pattern  
- Configurable precision, max input, and directories  
- CI/CD pipeline enforcing 90% coverage

---

## Configuration (.env)
CALCULATOR_LOG_DIR=./logs  
CALCULATOR_HISTORY_DIR=./history  
CALCULATOR_LOG_FILE=./logs/calculator.log  
CALCULATOR_HISTORY_FILE=./history/history.csv  
CALCULATOR_MAX_HISTORY_SIZE=1000  
CALCULATOR_AUTO_SAVE=true  
CALCULATOR_PRECISION=6  
CALCULATOR_MAX_INPUT_VALUE=1e12  
CALCULATOR_DEFAULT_ENCODING=utf-8  

---

## Installation & Setup
1. Clone the repository  
   git clone https://github.com/ishanr83/is601-midterm.git && cd is601-midterm  
2. Create and activate virtual environment  
   python -m venv venv && source venv/Scripts/activate  
3. Install dependencies  
   pip install --upgrade pip && pip install -r requirements.txt  
4. Run the application  
   python -m app  

---

## Commands
add, subtract, multiply, divide, power, root, modulus, int_divide, percent, abs_diff, history, undo, redo, clear, save, load, help, exit  

---

## Testing & Coverage
pytest --cov=app --cov-fail-under=90  
→ 96% coverage (25/25 tests passed)  

---

## CI/CD
GitHub Actions runs tests automatically on push.  
Fails if coverage < 90%. Uses Python 3.12.  

---

## Summary
✅ Functionality: All required + optional features  
✅ Code Quality: Modular, documented  
✅ Testing: 96% coverage  
✅ Logging & Auto-save: Implemented  
✅ CI/CD: Passing  
✅ Optional: Color CLI output  
