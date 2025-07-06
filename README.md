# typing-speed-tracker

A Python-based command-line application for testing and tracking your typing speed using difficulty-based text samples.

## Features

- 📄 Three difficulty levels: easy, medium, and hard
- ⌨️ Real-time typing speed test with timer
- 🧠 Calculates words per minute (WPM) and accuracy
- 🗃 Saves your latest result to `score.txt`
- ✅ Simple to use and beginner-friendly Python project

## How It Works

The program randomly selects a line from a text file (`easy.txt`, `medium.txt`, or `hard.txt`) depending on the level you choose. You then type the same text as fast and accurately as possible. At the end, you get your WPM and accuracy, and your result is saved.

## Installation

### Prerequisites

- Python 3.x installed on your system  
  👉 You can download Python from https://www.python.org/downloads/

### Clone the Repository

```bash
git clone https://github.com/Mouaz7/typing-speed-tracker.git
cd typing-speed-tracker
```

### Run the Program

```bash
python3 main.py
```

### Run the Test Script

```bash
python3 test.py
```

## Project Structure

```
typing-speed-tracker/
├── easy.txt          # Easy level text samples
├── medium.txt        # Medium level text samples
├── hard.txt          # Hard level text samples
├── main.py           # Main application logic
├── test.py           # Test runner for checking accuracy
├── score.txt         # Automatically saved score after a test
└── README.md         # Project description and usage
```

## Sample Output

```
Difficulty (easy/medium/hard): easy
Type the following:

The quick brown fox jumps over the lazy dog

Your input:
The quick brown fox jumps over the lazy dog

✅ Correct!
Time taken: 10.5 seconds
WPM: 51.43
Accuracy: 100.00%
Score saved to score.txt
```

## License

This project is open-source and free to use. No license restrictions applied.
