# Snake Game

A classic Snake game implemented in Python using Pygame.

## Features

- **Smooth gameplay** with arrow key controls
- **Progressive difficulty** - speed increases as you eat food
- **Score tracking** and snake length display
- **Game states** - menu, playing, and game over screens
- **Collision detection** for walls and self-collision
- **Restart functionality** - play multiple rounds without restarting

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Run the game:
```bash
python snake_game.py
```

## How to Play

### Controls
- **Arrow Keys**: Control the snake's direction (↑ ↓ ← →)
- **SPACE**: Start game / Play again after game over
- **ESC**: Pause game and return to menu

### Gameplay
1. Use arrow keys to control the green snake
2. Eat the red food to grow longer and increase your score
3. Avoid hitting the walls or the snake's own body
4. The game speed increases as you eat more food
5. Try to achieve the highest score possible!

### Scoring
- **+10 points** for each food item eaten
- **Final score** and snake length displayed on game over

## Game States

- **Menu**: Starting screen with instructions
- **Playing**: Active gameplay
- **Game Over**: Score display with restart options

Enjoy playing Snake! 🐍