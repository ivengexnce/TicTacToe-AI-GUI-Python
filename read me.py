# all necessary files for the Tic Tac Toe AI GUI project

import os

# Define main folder and subfolders
project_name = "TicTacToe-AI-GUI-Python"
asset_files = [
    "draw_sound.mp3",
    "click_sound.mp3",
    "win_sound.mp3",
    "button-pressed-38129.mp3",
    "hover_sound.mp3",
    "bang-140381.mp3",
    "error_sound.mp3",
    "closing_sound.mp3"
]

folders = [project_name, f"{project_name}/assets"
]

# File contents
readme_content = """
# 🎮 Tic Tac Toe AI Game (Python GUI)

A powerful and interactive Tic Tac Toe game built with Python's Tkinter for GUI and Pygame for immersive sound effects. Supports Player vs Player and Player vs AI gameplay with smart AI using the Minimax algorithm.

## 🚀 Features

- 🎮 **Two Game Modes**: 1v1 or vs AI
- 🧠 **AI Difficulty Levels**:
  - Easy: Random Moves
  - Moderate: Semi-intelligent
  - Hard: Minimax Algorithm (Unbeatable)
- 🔊 **Sound Effects**: Click, win, draw, hover, and intro sounds
- 🌓 **Light Theme** with hover highlights
- 📛 **Custom Player Names**
- 🖱️ **Hover Interactions** and Animated Win Sequences
- 🔇 **Sound Toggle Button**
- 💾 **Clean Code with Modular Functions**

## 🖼️ Screenshot



## 🛠️ Requirements

- Python 3.x
- Pygame
- Tkinter (comes built-in with Python)

Install pygame if not already installed:

```bash
pip install pygame
```
"""

# Create folders and files
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Create README.md
with open(f"{project_name}/README.md", "w") as readme_file:
    readme_file.write(readme_content)

# Add asset files
for asset in asset_files:
    open(f"{project_name}/assets/{asset}", "w").close()
