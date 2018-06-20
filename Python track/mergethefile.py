
###PROBLEM
'''
Consider the following:

A string, , of length  where .
An integer, , where  is a factor of .
We can split  into  subsegments where each subsegment, , consists of a contiguous block of  characters in . Then, use each  to create string  such that:

The characters in  are a subsequence of the characters in .
Any repeat occurrence of a character is removed from the string such that each character in  occurs exactly once. In other words, if the character at some index  in  occurs at a previous index  in , then do not include the character in string .
Given  and , print  lines where each line  denotes string .
'''


from collections import OrderedDict


def merge_the_tools(string, k):
    # your code goes here
    split = int(len(string) / k)

    i = 0
    while (i <= len(string)):
        temp = string[i:i + int(len(string) / split)]
        print("".join(OrderedDict.fromkeys(temp)))

        i = i + int(len(string) / split)