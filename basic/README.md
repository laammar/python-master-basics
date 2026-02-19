# Python Basics — Guess the Number Game

This project is an introductory Python exercise developed during the initial programming module of my Data Science master’s program.

The objective was to build an interactive number guessing game while practicing fundamental programming concepts and basic modularization.

---

## Project Structure

The project is composed of two main files located in the same directory:

### 1️⃣ Adivina_El_Numero_Carlos_Lara.ipynb

This Jupyter Notebook manages:

- User interaction
- Menu navigation
- Game mode selection
- Execution flow of the program

The notebook serves as the execution layer of the project.

---

### 2️⃣ Funciones.py

This Python file contains the core game logic, including:

- Game modes (single-player and two-player)
- Difficulty handling
- Scoring system
- Statistics tracking
- Helper functions used by the game

It acts as a custom Python module that separates logic from execution.

---

## How the files interact

The notebook imports the module using:

```python
import Funciones
