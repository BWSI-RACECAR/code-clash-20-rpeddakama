"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2022

Code Clash #20 - Tic Tac Toe (tictactoe.py)


Author: Carter Berlind

Difficulty Level: 9/10

Prompt: Alexander challenges you to a game of Tic Tac Toe. Knowing the success of computers 
in games such as chess and go, you decide to give computers the much more challenging task of 
playing Tic Tac Toe. Your task is to create a function that, when given two positions on a 
Tic Tac Toe board, finds a square that completes it. If there is no square, return that 0. 
Inputs should be 2 integers from 1-9 representing position as shown below.

1   2   3
4   5   6
7   8   9

The output should be an integer representing a position on the board.

Constraints: If input integers are outside of this range, return the string “invalid”

Test Cases:
Input: 1,5;     Output: 9
Input: 2,3;     Output: 1
Input: 6,8;     Output: 0
Input: 7,3;     Output: 5
Input: 1,7;     Output: 4
"""


def inRange(x, y, h, w):
    return x < h and y < w and x >= 0 and y >= 0


class Solution:
    def tic_tac_toe(self, row, col):
        key = [
            [0, 3, 2, 7, 9, 0, 4, 0, 5],
            [3, 0, 1, 0, 8, 0, 0, 5, 0],
            [2, 1, 0, 0, 7, 9, 5, 0, 6],
            [7, 0, 0, 0, 6, 5, 1, 0, 0],
            [9, 8, 7, 6, 0, 4, 3, 2, 1],
            [0, 0, 9, 5, 4, 0, 0, 0, 3],
            [4, 0, 5, 1, 3, 0, 0, 9, 8],
            [0, 5, 0, 0, 2, 0, 9, 0, 7],
            [5, 0, 6, 0, 1, 3, 8, 7, 0],
        ]

        if row < 10 and row > 0 and col < 10 and col > 0:
            return key[row - 1][col - 1]
        else:
            return "Invalid"


def main():
    num1 = int(input())
    num2 = int(input())

    tc1 = Solution()
    ans = tc1.tic_tac_toe(num1, num2)
    print(ans)


if __name__ == "__main__":
    main()
