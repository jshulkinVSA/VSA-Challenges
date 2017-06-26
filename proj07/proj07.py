# Name:
# Date:

# proj07: Word Game

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k':
        5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u':
        1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
WORDLIST_FILENAME = "words.txt"


def load_words():
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist


def get_frequency_dict(sequence):
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq


def get_word_score(word, n):
    word_score = 0
    for letter in word:
       word_score = word_score+SCRABBLE_LETTER_VALUES[letter]
    word_score = word_score*len(word)
    if n == len(word):
        word_score = word_score+50
    return word_score


def display_hand(hand):
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,
    print


def deal_hand(n):
    hand={}
    num_vowels = n / 3
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
    for i in range(num_vowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
    return hand


def update_hand(hand, word):
    updated_hand = hand.copy()
    for letter in word:
        if letter in hand:
            updated_hand[letter]=updated_hand[letter]-1
    return updated_hand


def is_valid_word(word, hand, word_list):
    copy_hand = hand.copy()
    word_copy = word
    answer = True
    if word not in word_list:
        answer = False
    for letter in word_copy:
        if letter in copy_hand:
            if copy_hand[letter] != 0:
                copy_hand[letter] = copy_hand[letter]-1
            else:
                answer=False
        elif letter not in copy_hand:
            answer = False
    return answer


def calculate_handlen(hand):
    handlen = 0
    for v in hand.values():
        handlen += v
    return handlen


def play_hand(hand, word_list):
    word = ""
    score = 0
    while HAND_SIZE != 0 and word != ".":
        print "Current Hand",
        display_hand(hand)
        word = raw_input("Enter word, or a '.' to indicate that you are finished: ")
        word = word.lower()
        validity = is_valid_word(word,hand, word_list)
        if validity is False and word != ".":
            print "That is not a valid word, try again"
        elif word != ".":
            score = score+get_word_score(word, HAND_SIZE)
            print word, "earned", get_word_score(word,HAND_SIZE), "points. Total:", score, "points"
            hand = update_hand(hand, word)
    print "Thanks for playing. You earned", score, "points."
    return score


def play_game(word_list):
    hand = deal_hand(HAND_SIZE)
    play_hand(hand, word_list)
    player_input = ""
    while player_input != "e":
        player_input = raw_input("Type 'n' to to play a new hand, type 'r' to replay hand, or type 'e' to exit the game: ")
        if player_input == "e":
            print "Thanks for playing."
            quit()
        elif player_input == "r":
            play_hand(hand, word_list)
        elif player_input == "n":
            hand= deal_hand(HAND_SIZE)
            play_hand(hand, word_list)

if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
