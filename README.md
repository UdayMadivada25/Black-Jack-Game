# 🃏 Blackjack Game 🎰

A **command-line Blackjack game** written in Python where you play against the **computer (banker)**. The game follows standard Blackjack rules, including **hit, stand, and bust mechanics**.

## 🎯 Features
- **Random card draws** for both the player and the banker.
- **Hit or stand option** to continue drawing or hold your hand.
- **Banker follows Blackjack rules**, stopping at 17+.
- **Automatic winner determination** based on hand values.
- **Card value calculations**, including **face cards (J, Q, K = 10) and Aces (1 or 11)**.

## 📜 Rules of Blackjack
1. The **goal** is to get as close to **21** without exceeding it.
2. Each player starts with **two random cards**.
3. The player can choose to **hit (draw a card)** or **stand (keep their hand)**.
4. Face cards (**J, Q, K**) are worth **10 points**, and **Aces** are **1 or 11**, depending on what is best for the player.
5. The banker will **continue drawing until they reach at least 17**.
6. **If a hand exceeds 21, that player busts** and loses the game.
7. The player with the **higher valid score** (≤ 21) wins.

## 🛠 Installation & Setup
1. **Clone the Repository**
   ```sh
   git clone https://github.com/UdayMadivada25/Black-Jack-Game.git
   cd Black-Jack-Game
