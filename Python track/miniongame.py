
### PROBLEM:
'''
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string .
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string .
'''


def minion_game(string):
    # your code goes here
    vowels = ['A', 'E', 'I', 'O', 'U']
    i = 0
    j = 0
    list = []
    stuartscore = 0;
    kevinscore = 0;
    for k in range(len(string)):
        if (string[k] in vowels):
            kevinscore = kevinscore + len(string) - k
        else:
            stuartscore = stuartscore + len(string) - k
    if (stuartscore > kevinscore):
        print('Stuart ' + str(stuartscore))
    elif (kevinscore > stuartscore):
        print('Kevin ' + str(kevinscore))
    else:
        print('Draw')
