# Chess ♟️

A basic terminal-based chess engine written in Python. This early prototype supports piece classes, a board representation, and partial movement logic—currently implemented for pawns only.

![chess pieces](https://upload.wikimedia.org/wikipedia/commons/thumb/7/72/Chess_Pieces_Sprite.svg/512px-Chess_Pieces_Sprite.svg.png)

## 🧠 Features
- Object-oriented design using Python classes
- Unicode symbols for visualizing pieces in the terminal
- Board printing with color using `colorama`
- Pawn movement logic including:
  - One and two-square advances
  - Captures (including `exd4` style notation)
- Input-based move handling
- Structured but unfinished parsing system for SAN-like notation

## 🚧 Work in Progress
The following components are either placeholders or partially implemented:
- Movement for Rook, Knight, Bishop, Queen, and King
- En passant, castling, and check/checkmate detection
- Game state management (turn validation, legal move enforcement)
- Board history and undo
