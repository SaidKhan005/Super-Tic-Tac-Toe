## Adding Power-Ups and Special Moves

As a Player, I want to enjoy an enhanced gaming experience in Super Tic Tac Toe by introducing an element of strategy to Super Tic Tac Toe.

- When I start a new game I should have the option to enable power-ups or special moves such as blocking an opponent's move or swapping symbols
- Each player should have access to a limited number of power-ups based on their rank on the leaderboard.
- Lower level player can also obtain power ups by spending in-game currency earned if they maintain a login streak.

## Implementation
- Modify the game logic to accommodate the use of power-ups during gameplay.
- Determine the conditions under which players can obtain power-ups, such as earning them through gameplay milestones like being top 5 in the leaderboard or purchase using in game currency
- Add logic for in game currency.
- Add logic to keep track of user login streaks
- Modify the necessary html templates to display power up buttons. This includes the current game template