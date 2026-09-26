# Ransomware Behavior Detector

## 1. About the Project
This is a Python project that checks a chosen folder for odd file activity.

The program takes two scans of the folder with a 30‑second pause. It looks for files that're new or changed and then calculates a risk score.

## 2. How It Works
1. The user types the folder path.
2. The program takes the scan.
3. It waits for 30 seconds.
4. The program takes the scan.
5. The two scans are compared.
6. The risk score is calculated.
7. The result is shown.
8. The result is written to `log.txt`.

## 3. Risk Calculation

The program uses rules to calculate the risk:
- 5 or more changed files → **+2 points**
- 1 or more new files → **+1 point**
The final outcome is:
- **0 points → SAFE**
- **1 point → SUSPICIOUS**
- **2 or more points → HIGH RISK**
For example if 5 files are changed and 1 new file is created the risk score becomes 3. The result is **HIGH RISK**.

## 4. Project Files
```text
VITYARTHIProject/

│
├── main.py
├── monitor.py
├── analyzer.py
├── alert.py
├── logger.py
├── test.py
├── README.md
└── test_folder/
```
### main.py
Runs the program takes the folder path from the user performs the two scans and shows the result.

### monitor.py
Scans the folder and stores the file names and their last modified times.

### analyzer.py
Compares the two scans. Calculates the risk score.

### alert.py
Displays the scan result. Shows a warning depending on the risk level.

### logger.py
Saves the result in `log.txt`.

## 5. Technologies Used
- Python
- `os` module
- `time` module
- Functions
- Loops
- Dictionaries
- File handling

## 6. Requirements
- Python 3
- No external libraries are needed.

## 7. Note
This is an educational project, for learning Python and file monitoring. It is not an antivirus or professional ransomware detection system.