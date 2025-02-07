
# SpaceWar

## Overview
SpaceWar is a simple 2D space battle game built using Python's `turtle` module. Players control a spaceship to maneuver around the game area, fire missiles, and interact with enemies and allies.

## Features
- Player spaceship with movement controls
- Enemies that move randomly
- Allies that also move randomly
- Missiles that can be fired to destroy enemies
- Collision detection between the player, enemies, allies, and missiles
- Score tracking system
- Particle effects for explosions
- Game border with status display
- Health system for the player's spaceship
- Power-ups for shields and weapon upgrades

## Installation
1. Ensure you have Python installed (Python 3 recommended).
2. Clone this repository:
   ```sh
   git clone https://github.com/evitabarboza/spaceWar.git
   ```
3. Navigate to the project directory:
   ```sh
   cd spaceWar
   ```
4. Run the game:
   ```sh
   python spacewar.py
   ```

## Controls
- **Left Arrow**: Rotate left
- **Right Arrow**: Rotate right
- **Up Arrow**: Accelerate
- **Down Arrow**: Decelerate
- **Spacebar**: Fire missile
- **P**: Pause/Resume
- **Esc**: Exit game

## How to Play
- Move your spaceship around the screen using the arrow keys.
- Fire missiles using the spacebar to destroy enemies and earn points.
- Avoid collisions with enemies, as they decrease your score.
- Avoid hitting allies, as it will also lower your score.
- Collect power-ups to enhance your shields and weapons.

## Dependencies
- Python 3.x
- `turtle` (included in standard Python library)

## Known Issues
- The game currently runs in an infinite loop and must be manually exited.
- Some object movements may need further fine-tuning.
- Collision detection may need improvement for fast-moving objects.

## Future Improvements
- Add levels and difficulty progression
- Implement a start screen and game-over screen
- Enhance explosion effects and animations
- Add sound effects
- Introduce multiplayer support

## License
This project is open-source and available under the MIT License.

## Author
Developed by [Evita Barboza](https://github.com/evitabarboza).

