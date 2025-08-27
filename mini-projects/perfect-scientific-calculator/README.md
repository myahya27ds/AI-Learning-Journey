# 🔢 Perfect Scientific Calculator (Python CLI)

A **Command Line Interface (CLI) based scientific calculator** that supports basic math operations, trigonometry, logarithms, and automatic expression evaluation.  
This calculator also comes with a **calculation history** feature that can be saved and cleared as needed.

---

## ✨ Features
- ✅ Arithmetic Operations: Addition, Subtraction, Multiplication, Division, Modulus, Exponentiation  
- ✅ Special Operations: Square Root, Logarithm (base 10)  
- ✅ Trigonometric Functions: Sin, Cos, Tan (choose **radians** or **degrees**)  
- ✅ Automatic calculation with expressions (example: `sqrt(16) + sin(pi/2)`)  
- ✅ Calculation history saved in `history.txt`  
- ✅ Interactive menu with options to view and clear history  

---

## 📂 Project Structure
```
.
├── calculator.py     # Main script
├── history.txt       # Calculation history (auto-generated)
└── README.md         # Documentation
```

---

## ▶️ How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/myahya27ds/AI-Learning-Journey/tree/6869458dcc4f8a0318ddc1930ae3ff0f9986c019/mini-projects/perfect-scientific-calculator
   cd perfect-scientific-calculator
   ```

2. Run the program with Python:
   ```bash
   python main.py
   ```

---

## 📖 Main Menu
| No | Menu                   | Description |
|----|------------------------|-------------|
| 1  | Automatic Calculation  | Directly evaluate an expression (example: `sqrt(25) + log(100)`) |
| 2  | Addition               | Addition |
| 3  | Subtraction            | Subtraction |
| 4  | Multiplication         | Multiplication |
| 5  | Division               | Division |
| 6  | Exponentiation         | Exponentiation |
| 7  | Modulus                | Remainder |
| 8  | Square Root            | Square root |
| 9  | Logarithm              | Logarithm base 10 |
| 10 | Sin                    | Sine |
| 11 | Cos                    | Cosine |
| 12 | Tan                    | Tangent |
| 13 | View History           | View calculation history |
| 14 | Clear History          | Clear history |
| 0  | Exit                   | Exit program |

---

## 🛠 Example Usage
```text
==== Perfect Scientific Calculator ====
1. Automatic Calculation
2. Addition
...
0. Exit

Choose menu: 1
Expression: sqrt(16) + log(100)
sqrt(16) + log(100) = 6
```

---

## 📝 Notes
- This program runs on **Python 3**.
- History is automatically saved in `history.txt`.
- To clear history, use the `Clear History` menu.

---

## 📜 License
MIT License – free to use, modify, and redistribute.
