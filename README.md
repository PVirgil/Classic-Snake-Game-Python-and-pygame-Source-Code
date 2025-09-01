# Classic Snake Game: Python and pygame Source Code

## Overview
This project is a simple implementation of the **classic Snake game** using [Pygame](https://www.pygame.org/).  
The game features a moving snake controlled by the arrow keys and demonstrates **real-time rendering, keyboard input handling, and basic game loops** in Python.

---

## Features
- **Classic Snake Movement**: Navigate the snake using arrow keys (Up, Down, Left, Right).
- **Real-Time Updates**: Smooth movement controlled by a game loop and adjustable speed.
- **Dynamic Snake Growth** *(optional extension)*: The foundation is laid for adding food collection and snake growth.
- **Collision Handling** *(to be added)*: Extendable to include self-collision and wall collision logic.
- **Customizable Gameplay**: Change speed, grid size, or snake color.

---

## Requirements
- Python 3.8+
- Pygame

Install dependencies with:
```bash
pip install pygame
```

---

## How to Run
1. Clone this repository or copy the script into a file named `snake_game.py`.
2. Run the script:
   ```bash
   python snake_game.py
   ```
3. Use the arrow keys to control the snake:
   - **Up Arrow**: Move Up
   - **Down Arrow**: Move Down
   - **Left Arrow**: Move Left
   - **Right Arrow**: Move Right

---

## Code Structure
- **Initialization**: Sets up Pygame, screen dimensions, and game variables.
- **Game Loop**: Continuously listens for events, updates the snake’s position, and renders the display.
- **Input Handling**: Arrow key inputs determine the snake’s direction.
- **Rendering**: Snake is drawn on the screen as green rectangles on a black background.

---

## Example Gameplay
- Snake starts at position `[100, 50]` and moves to the right by default.
- Direction changes are handled smoothly while preventing reverse-direction crashes.
- Game updates occur at **15 frames per second** (adjustable).

---

## Potential Enhancements
This implementation provides the **core mechanics** of Snake. Suggested improvements:
- Add **food objects** that increase the snake’s length when eaten.
- Implement **score tracking**.
- Add **collision detection** with walls and self-body for a proper game-over mechanic.
- Introduce **levels or increasing difficulty** by raising the snake’s speed over time.

---

## Example Output
Running the script launches a **600x400 window** with:
- **Black background**
- **Green snake** moving in the chosen direction
- Real-time keyboard controls
