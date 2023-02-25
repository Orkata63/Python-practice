#solution that works bu#https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true
#solution that works but doesnt meet time constraints logically i will be trying to compine the 2 funtions into 1
#version 2 also not meeting time constraints
#for version 3 will try using a comination import module PS. also doesnt work maybe i need to revisit the counting function
#Math is nice we can show its as a 1 time combination of the original word that would be the (lenght-1)+lenght which represents the total and since theres less vowels we'll check on vowels only
#actually we can just guess that the n index has all the unique combinations since were not having any repetitions meaning theres no need to check
#import string as st
#import itertools


"""
def count_substring(string, sub_string):      # code from a previous challenge problem 23
    counter = 0
    for x in range(0,len(string)-len(sub_string)+1):
        if string[x:x+len(sub_string)] == sub_string:
            counter+=1
    return counter
"""


def minion_game(string):
# your code goes here

    Vowels = ["A", "E", "I", "O", "U"]  # Y is not considered a vowel in the challenge
    #Consonants = set(st.ascii_uppercase).symmetric_difference(Vowels)
    #uniq = set()

    valueV = 0
    valueC = 0

    for i in range(len(string)):
        if string[i] in Vowels:
            valueV += len(string)-i
        else:
            valueC += len(string)-i
    if valueV > valueC:
        print("Kevin " + str(valueV))
    elif valueV < valueC:
        print("Stuart " + str(valueC))
    else:
        print("Draw")


if __name__ == '__main__':
    s = input()
    minion_game(s)
    """
        def vowelL():
            numV = 0
            uniq = set()
            for indexy, y in enumerate(string):
                sub_string = ""
                if y in Vowels:
                    for n in string[indexy:]:
                        sub_string += n
                        if sub_string not in uniq:
                            numV += count_substring(string, sub_string, indexy)
                            uniq.add(sub_string)
            return numV
        def consonantsL():
            numC = 0
            uniq = set()
            for indexy, y in enumerate(string):
                sub_string = ""
                if y in Consonants:
                    for n in string[indexy:]:
                        sub_string += n
                        if sub_string not in uniq:
                            numC += count_substring(string, sub_string, indexy)
                            uniq.add(sub_string)
            return numC

        Vowels = ["A", "E", "I", "O", "U"] # Y is not considered a vowel in the challenge
        Consonants = set(st.ascii_uppercase).symmetric_difference(Vowels)
        valueV = vowelL()
        valueC = consonantsL()
    """  #version 1

    """
        for indexy, y in enumerate(string):
        sub_string = ""
        if y in Vowels:
            for n in string[indexy:]:
                sub_string += n
                if sub_string not in uniq:
                    valueV += count_substring(string, sub_string, indexy)
                    uniq.add(sub_string)
        if y in Consonants:
            for n in string[indexy:]:
                sub_string += n
                if sub_string not in uniq:
                    valueC += count_substring(string, sub_string, indexy)
                    uniq.add(sub_string)
                    """ #version 2 logic