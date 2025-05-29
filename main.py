import pyautogui
import time
from PIL import ImageGrab, ImageOps
import numpy as np
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Set dynamic position
logging.info("Place the cursor near the dinosaur. You have 5 seconds...")
time.sleep(5)
DINOSAUR_X, DINOSAUR_Y = pyautogui.position()
logging.info(f"Dinosaur position detected at: X={DINOSAUR_X}, Y={DINOSAUR_Y}")

# Define the obstacle region relative to the dinosaur's position
OBSTACLE_REGION = (DINOSAUR_X + 80, DINOSAUR_Y - 20, DINOSAUR_X + 300, DINOSAUR_Y + 70)

def jump():
    """Press the spacebar to make the dinosaur jump."""
    logging.info("Jumping!")
    pyautogui.press("space")

def detect_obstacle(region):
    """
    Detect obstacles by analyzing a specific region of the screen.
    Returns True if an obstacle is detected.
    """
    screenshot = ImageGrab.grab(region)  # Capture the game area
    grayscale = ImageOps.grayscale(screenshot)  # Convert to grayscale
    pixel_array = np.array(grayscale)  # Convert to NumPy array
    pixel_sum = pixel_array.sum()  # Calculate pixel intensity sum
    return pixel_sum < 5000  # Threshold to determine if an obstacle exists

def main():
    """Main function to automate the Google Dinosaur Game."""
    logging.info("Starting the Dinosaur Game Bot. Switch to the browser and start the game!")
    time.sleep(3)  # Allow time to switch to the game

    try:
        while True:
            if detect_obstacle(OBSTACLE_REGION):
                jump()
            time.sleep(0.05)  # Adjust the delay as per the game's speed
    except KeyboardInterrupt:
        logging.info("Bot stopped by user.")

if __name__ == "__main__":
    main()



                                                                                                                                                             