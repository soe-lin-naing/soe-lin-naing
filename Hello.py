import os
import time


def clear():
    os.system("cls" if os.name == "nt" else "clear")


heart_lines = [
    "                 __                 ",
    "             .-\"  \"-.              ",
    "           .'  .-.  '.             ",
    "          /   /   \\   \\            ",
    "         |   |   |   |            ",
    "         |   |   |   |            ",
    "          \\   \\_._/   /            ",
    "           '._     _.'             ",
    "              `-._.-'              ",
    "            .-" "-.                ",
    "           /  .-. .\\               ",
    "          /  /   \\ \\               ",
    "         |  |     | |              ",
    "         |  |     | |              ",
    "          \\  \\   / /               ",
    "           '._`-._.'               ",
    "              `-._.'                ",
    "                 |                  ",
    "                 |                  ",
]

# Use a cleaner heart silhouette for consistent rendering in terminal.
heart_lines = [
    "       ***       ",
    "     *****      ",
    "   *********    ",
    "  ***********   ",
    "  ************  ",
    "  ************  ",
    "   **********   ",
    "    ********    ",
    "     ******     ",
    "      ****      ",
    "       **       ",
]

# Full heart shape with deeper silhouette
heart_shape = [
    "      ***       ",
    "    *******     ",
    "   *********    ",
    "  ***********   ",
    "  ************  ",
    "  ************  ",
    "   **********   ",
    "    ********    ",
    "     *******    ",
    "      *****     ",
    "       ***      ",
    "        *       ",
]

# Real heart silhouette using filled blocks
heart_fill = [
    "       ***       ",
    "     *******     ",
    "   ***********   ",
    "  *************  ",
    "  ************** ",
    "  ************** ",
    "   ************  ",
    "    **********   ",
    "     ********    ",
    "      ******     ",
    "       ****      ",
    "        **       ",
    "         *       ",
]

for frame in range(len(heart_fill) + 1):
    clear()
    for y, line in enumerate(heart_fill):
        filled = line
        if y >= len(heart_fill) - frame:
            filled = line.replace("*", "\033[31m♥\033[0m")
        print(filled.center(30))
    time.sleep(0.12)

print("\n\033[31m❤️ Love you ❤️\033[0m")
