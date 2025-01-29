# FF_ISM_Simulation
# FFISM vs. FISM Simulation

This repository contains the simulation code for comparing **Fermatean Fuzzy Interpretive Structural Modeling (FFISM)** with **Fuzzy ISM (FISM)** using the **Dice-Sørensen Similarity (DSS) metric**.

## 📌 Overview
The simulation aims to validate the structural consistency between FFISM and FISM by generating decision matrices, computing reachability matrices, and measuring their similarity using DSS. The results help assess the robustness and applicability of FFISM in interpretive structural modeling.

## 📂 Files
- **`ffism_fism_simulation.py`** – Main simulation script.
- **`Figure_1.png`** – Boxplot visualization of the DSS results.
- **`README.md`** – This document.

## ⚙️ Installation
Ensure you have **Python 3.x** and the required dependencies installed:
```bash
pip install numpy matplotlib
```

## 🚀 Usage
Run the simulation by executing:
```bash
python ffism_fism_simulation.py
```
The script will prompt for the number of replications and generate statistical results along with a DSS boxplot.

## 📊 Results
The simulation was conducted with **10,000 replications**, yielding a **mean DSS of 0.91** and **SD of 0.04**, confirming the structural consistency between FFISM and FISM.

## 📜 Citation
If you use this code, please cite:
- Ghasemian Sahebi et al. (2024) for FISM.
- Dice (1945) and Sørensen (1948) for DSS.

## 🛠️ License
This project is released under the **MIT License**.

## 📬 Contact
For inquiries or contributions, feel free to reach out!

---
Happy coding! 🚀

