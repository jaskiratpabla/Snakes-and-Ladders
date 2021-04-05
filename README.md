# Snakes-and-Ladders
Snakes and Ladders in Python, full documentation and testing is included.
The function make_board(snakes, ladders, board) consumes nested lists snakes, ladders and board. The first two consumed lists are lists of lists of integers. Each integer is the number of a cell in a 10 by 10 board where cells are numbered as shown below:

![image](https://user-images.githubusercontent.com/67871488/113639211-abda0000-9646-11eb-9403-a71dd8f353c1.png)

No integer will appear more than once across both the consumed lists. Put another way, [snakes]+[ladders] won't contain any duplicates. 

The parameter board will be a list of list of strings representing an empty 10 by 10 board. That is, the outer list and each inner list will have length 10 and each string will be "." (a period). To help with your testing, we have provided a function empty_board which produces this value.

The function returns None and mutates board so that each string in board:
- becomes the letter "S" if the number of the cell appears in snakes,
- becomes the letter "L" if the number of the cell appears in ladders, or
- is unchanged otherwise.
