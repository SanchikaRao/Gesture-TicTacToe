# 🎮 Gesture Tic-Tac-Toe

> **A touchless Tic-Tac-Toe game controlled entirely through hand gestures using a webcam.**

Gesture Tic-Tac-Toe transforms the classic game into an interactive computer-vision experience. Instead of using a mouse or keyboard, players interact with the game board using **real-time hand gestures detected through a webcam**.

The project uses **Python, OpenCV, and MediaPipe's Hand Landmarker** to track hand movements and translate them into game actions.

---

## ✨ Features

* 🖐️ **Gesture-based interaction** — Play without a mouse or keyboard.
* 📷 **Real-time webcam tracking** — Uses the camera to detect hand movements.
* 🎯 **Hand landmark detection** — Tracks hand geometry using MediaPipe.
* 🎮 **Classic Tic-Tac-Toe gameplay** — Includes win and draw conditions.
* ⚡ **Real-time interaction** — Gesture detection and game updates happen instantly.
* 🖥️ **Computer-vision based UI** — Game interaction is integrated with the camera feed.

---

## 🧠 How It Works

The project follows a simple computer-vision pipeline:

```text
        ┌──────────────┐
        │    Webcam    │
        └──────┬───────┘
               │
               ▼
        ┌──────────────┐
        │    OpenCV    │
        │ Frame Capture│
        └──────┬───────┘
               │
               ▼
        ┌──────────────────┐
        │     MediaPipe    │
        │ Hand Landmarker  │
        └────────┬─────────┘
                 │
                 ▼
        ┌──────────────────┐
        │ Hand Landmark /  │
        │ Gesture Detection│
        └────────┬─────────┘
                 │
                 ▼
        ┌──────────────────┐
        │ Tic-Tac-Toe Game │
        │     Logic        │
        └────────┬─────────┘
                 │
                 ▼
        ┌──────────────────┐
        │   Game Output    │
        └──────────────────┘
```

### Workflow

1. The webcam continuously captures video frames.
2. OpenCV processes the camera feed.
3. MediaPipe detects and tracks hand landmarks.
4. The detected hand position/gesture is interpreted as player input.
5. The corresponding Tic-Tac-Toe cell is selected.
6. The game updates the board and checks for a winner or draw.

---

## 🛠️ Tech Stack

| Technology        | Purpose                                |
| ----------------- | -------------------------------------- |
| 🐍 **Python**     | Core programming language              |
| 👁️ **OpenCV**    | Webcam access and frame processing     |
| 🖐️ **MediaPipe** | Hand landmark detection                |
| 🎮 **Game Logic** | Board state, turns, win/draw detection |

---

## 📂 Project Structure

```text
Gesture-TicTacToe/
│
├── game.py
├── hand_landmarker.task
├── .gitignore
└── README.md
```

### `game.py`

Contains the main application logic, including webcam handling, hand tracking, gesture-based interaction, and Tic-Tac-Toe gameplay.

### `hand_landmarker.task`

MediaPipe hand-landmark model used for real-time hand tracking.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/SanchikaRao/Gesture-TicTacToe.git
```

### 2. Navigate to the project

```bash
cd Gesture-TicTacToe
```

### 3. Install dependencies

Make sure Python is installed, then install the required libraries:

```bash
pip install opencv-python mediapipe
```

### 4. Run the game

```bash
python game.py
```

Make sure your **webcam is connected and accessible** before starting the application.

---

## 🎮 How to Play

1. Start the application.
2. Allow webcam access if prompted.
3. Position your hand in front of the camera.
4. Use your hand movement/gesture to interact with the board.
5. Select cells and make your moves.
6. Continue until a player wins or the game ends in a draw.

---

## 💡 Why This Project?

Traditional games rely on physical input devices such as keyboards, mice, or touchscreens.

This project explores how **computer vision can be used as a natural human-computer interaction method**, replacing conventional controls with hand gestures.

It combines:

**Computer Vision + Gesture Recognition + Game Development**

into one interactive application.

---

## 🔮 Future Improvements

* [ ] Add multiple gesture types for different actions
* [ ] Add single-player mode with an AI opponent
* [ ] Improve gesture recognition accuracy
* [ ] Add difficulty levels
* [ ] Add sound effects and animations
* [ ] Add score tracking
* [ ] Add multiplayer mode
* [ ] Create a more polished graphical interface
* [ ] Add gesture calibration for different lighting conditions

---

## 📸 Demo

> Add screenshots or a short GIF of the gameplay here.

```text
📷 Webcam + Hand Tracking
        ↓
🎮 Gesture Selection
        ↓
❌⭕ Tic-Tac-Toe Board
```

A gameplay GIF would make this repository much more attractive to recruiters and hackathon judges.

---

## 🌟 Key Learning Outcomes

Through this project, I explored:

* Real-time computer vision
* Hand landmark detection
* Gesture-based human-computer interaction
* Webcam frame processing
* Game-state management
* Python application development
* Integrating MediaPipe with OpenCV

---

## 👩‍💻 Author

**Sanchika Rao**

GitHub: [@SanchikaRao](https://github.com/SanchikaRao)

---

## ⭐ Support

If you found this project interesting, consider giving the repository a ⭐!

Made with 🐍 Python, 👁️ OpenCV & 🖐️ MediaPipe.
