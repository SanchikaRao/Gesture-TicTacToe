import cv2
import mediapipe as mp
import numpy as np
import os

# Ensure the model file is present
if not os.path.exists("hand_landmarker.task"):
    print("ERROR: Please download 'hand_landmarker.task' and place it in this folder!")
    exit()

# Setup Game State
board = [["" for _ in range(3)] for _ in range(3)]
current_player = "X"
game_over = False
winner_text = ""
cooldown_counter = 0  # Prevents rapid double placement

# Setup MediaPipe Options
BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

options = HandLandmarkerOptions(
    base_options=BaseOptions(model_asset_path="hand_landmarker.task"),
    running_mode=VisionRunningMode.IMAGE,
    num_hands=1
)

cap = cv2.VideoCapture(0)
print("True Gesture System Online! 2 Fingers = X | 5 Fingers = O | Fist = Reset")

with HandLandmarker.create_from_options(options) as landmarker:
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape
        cell_w, cell_h = w // 3, h // 3

        if cooldown_counter > 0:
            cooldown_counter -= 1

        # Convert image to MediaPipe Format
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        detection_result = landmarker.detect(mp_image)

        # Draw Tic-Tac-Toe Grid
        for i in range(1, 3):
            cv2.line(frame, (cell_w * i, 0), (cell_w * i, h), (200, 200, 200), 2)
            cv2.line(frame, (0, cell_h * i), (w, cell_h * i), (200, 200, 200), 2)

        # Draw Board Markers
        for r in range(3):
            for c in range(3):
                if board[r][c] == "X":
                    cv2.putText(frame, "X", (c*cell_w + 60, r*cell_h + 140), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 50, 50), 5)
                elif board[r][c] == "O":
                    cv2.putText(frame, "O", (c*cell_w + 60, r*cell_h + 140), cv2.FONT_HERSHEY_SIMPLEX, 3, (50, 50, 255), 5)

        gesture = "No Hand Detected"

        # Process hand coordinates safely if a hand is visible
        if detection_result.hand_landmarks:
            hand_landmarks = detection_result.hand_landmarks[0]

            # Track Index Finger Tip (Landmark 8)
            ix = int(hand_landmarks[8].x * w)
            iy = int(hand_landmarks[8].y * h)
            
            # Map location to board grid
            col = max(0, min(2, ix // cell_w))
            row = max(0, min(2, iy // cell_h))

            # Highlight the box your hand is hovering over
            if not game_over:
                cv2.rectangle(frame, (col*cell_w, row*cell_h), ((col+1)*cell_w, (row+1)*cell_h), (0, 255, 255), 3)
            
            # Draw a visual feedback circle over your index finger tip
            cv2.circle(frame, (ix, iy), 12, (0, 255, 0), -1)

            # --- COUNT EXTENDED FINGERS ---
            tips = [8, 12, 16, 20]
            open_fingers = 0
            
            # Check Thumb
            if hand_landmarks[4].x > hand_landmarks[3].x: 
                open_fingers += 1
            # Check Index, Middle, Ring, Pinky
            for tip in tips:
                if hand_landmarks[tip].y < hand_landmarks[tip - 2].y:
                    open_fingers += 1

            # Match finger configuration to actions
            if open_fingers == 2:
                gesture = "PEACE SIGN (Spawn X)"
                if not game_over and current_player == "X" and board[row][col] == "" and cooldown_counter == 0:
                    board[row][col] = "X"
                    current_player = "O"
                    cooldown_counter = 20  # Set temporary placement cooldown
            elif open_fingers >= 4:
                gesture = "OPEN HAND (Spawn O)"
                if not game_over and current_player == "O" and board[row][col] == "" and cooldown_counter == 0:
                    board[row][col] = "O"
                    current_player = "X"
                    cooldown_counter = 20
            elif open_fingers == 0:
                gesture = "CLOSED FIST (Reset Mode)"
                if game_over:
                    board = [["" for _ in range(3)] for _ in range(3)]
                    game_over = False
                    winner_text = ""
                    current_player = "X"

            # Check Win/Tie Conditions
            for i in range(3):
                if board[i][0] == board[i][1] == board[i][2] != "": game_over, winner_text = True, f"Player {board[i][0]} Wins!"
                if board[0][i] == board[1][i] == board[2][i] != "": game_over, winner_text = True, f"Player {board[0][i]} Wins!"
            if board[0][0] == board[1][1] == board[2][2] != "": game_over, winner_text = True, f"Player {board[0][0]} Wins!"
            if board[0][2] == board[1][1] == board[2][0] != "": game_over, winner_text = True, f"Player {board[0][2]} Wins!"
            if not game_over and all(cell != "" for r in board for cell in r): game_over, winner_text = True, "It's a Tie!"

        # HUD Layer
        cv2.putText(frame, f"Gesture: {gesture}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)
        if game_over:
            cv2.putText(frame, winner_text, (50, h // 2), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 250, 0), 5)
            cv2.putText(frame, "Make a Fist to Reset", (50, (h // 2) + 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        cv2.imshow('100% True Gesture Tic-Tac-Toe', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()