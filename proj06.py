# Name: Jeffrey, Bonnie
# Date:6/22/18


# proj06: Hangman

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program

wordlist = load_words()

# your code begins here!


def hangman():

    randomword = choose_word(wordlist)
    correctword = (randomword)
    list3=[]#actual list for a bunch of blanks

    #while list3!=correctword:




        # list1=[]
    blanks = []
    list4=['-']

    for letters in correctword:
        blanks.append(letters)

    wordlength2=len(blanks)
    wordlength=len(correctword)
    wordlength3 = len(list3)#setting the lenghth of what the blanks are naming it
    while wordlength3 < wordlength:
        list3.append('-')
        wordlength3 = wordlength3+1
    print list3
    guesses = 8
    while list3 != correctword:

        playerinput = raw_input("Enter your letter!")
        index=0
        allwrong = True
        guesses = guesses - 1
        print "you have guessed..."
        print guesses
        print "...times so far. you can have 8 total guesses."
        if guesses == 8:
            print " O"
            print "/|\"
            print " /\"
        if guesses == 6:
            print " O"
            print "/|\"
            print " /"
        if guesses == 4:
            print "0"
            print '|'
        if guesses == 2:
            print "0"
        if guesses == 0:
            print "sorry! you are out of guesses."
            print "Game Over."
            quit()
        while index < wordlength3:


            if playerinput == correctword[index]:
                list3[index] = playerinput

                allwrong = False




            index = index + 1

        list4.append(playerinput)
        if allwrong == True:
            print "Sorry, that's wrong..."
        else:
            print "Yep, ya got it! Guess another letter!"
        print 'Would you like to take a guess?'
        guessyesorno = raw_input ('yes or no')
        if guessyesorno == "yes" or guessyesorno == 'Yes' or guessyesorno == 'YES' or guessyesorno == 'yep':

            userinput2 = raw_input("Whats the word?")
            if userinput2 == randomword:
                print "That is correct! do you wanna play again?"
                input2 = raw_input ("yes or no")
                if input2 == "no" or input2 == 'No' or input2 == "NO" or input2 == 'nope':
                    quit()
                if input2 == "yes" or input2 == 'Yes' or input2 == 'YES' or input2 == 'yep':
                    hangman()
        if guessyesorno == "no" or guessyesorno == 'No' or guessyesorno == "NO" or guessyesorno == 'nope':
            print "okay. we can keep guessing letters."
        elif userinput2!= randomword:
            print "sorry, that is wrong."


        #print blanks
        print list3
        print list4


        if list3 == blanks:
            print "Congrats, you win! Game Over."
            print "Do you wanna play again?"
            input= raw_input ("yes or no?")
            if input == "no":
                quit()
            if input == "yes":
                hangman()
hangman()










    #while wordlength3 < wordlength:
        #list3.append('-')
        #indexnumber = 0
        #while indexnumber < wordlength:
            #indexnumber = indexnumber + 1
            #print list3




    #print blanks
    #print len(blanks)

    #for letters in (correctword):

        #if playerinput == correctword[indexnumber]: #this part is for placing correct letters

            #wordlength3 = len(list3)


        #else:
            #while indexnumber < wordlength:
                #indexnumber = indexnumber + 1
        #list4.append(playerinput)
        #print list4