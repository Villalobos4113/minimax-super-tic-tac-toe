# Super Tic-Tac-Toe AI

## Overview

This project implements a Super Tic-Tac-Toe playing machine, developed for an Artificial Intelligence class at ITAM (Instituto Tecnológico Autónomo de México). It uses the Minimax algorithm to strategize against human players.

## Features
- Minimax Algorithm: Implements Minimax for intelligent AI decision-making.
- User Interface: An interactive interface for playing against the AI.
- Difficulty Levels: Offers adjustable difficulty via Minimax search depth.

## Installation

### Prerequisites
Ensure you have Python 3.x installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Setting Up a Virtual Environment (Opcional)
It's recommended to use a virtual environment to avoid conflicts with other projects. 

1. Install virtualenv
   ```bash
   python -m pip install --user virtualenv
   ```
2. Create a virtual environment:
   ```bash
   virtualenv venv
   ```
3. Activate the environment:
   - Windows
     ```bash
     .\venv\Scripts\activate
     ```
   - Linux o Mac
     ```bash
     source venv/bin/activate
     ```

### Installing Dependencies

Install required packages:
```bash
pip install -r requirements.txt
```

If installed packages add them to requirements.txt. To add all pip packages:
```bash
pip freeze > requirements.txt
```

## Usage
Start the game:
```bash
python main.py
```
Follow on-screen instructions to play.

## Contributing
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/YourFeature`).
3. Commit changes (`git commit -m 'Add YourFeature`').
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## Authors
- Fernando Villalobos Betancourt [@Villalobos4113](https://www.github.com/Villalobos4113)
- Valeria Anahí Andrade Maqueda [@valmaqueda29](https://github.com/valmaqueda29)
- Rafael Alejandro Bautista Baca [@Osopole117](https://github.com/Osopole117)

## License
This project is under the MIT License - see [LICENSE](https://choosealicense.com/licenses/mit/) for details.