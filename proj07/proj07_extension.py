# Name: Reid and Jeffrey
# Date: 6/26/17

# proj07 Extension

from proj07 import *
from perm import *


def comp_choose_word(hand, word_list):
    comp_lst_1 = []
    max = 0
    for number in range (1, HAND_SIZE+1):
        words = get_perms(hand, number)
        for word in words:
            if is_valid_word(word, hand, word_list) is True and word not in comp_lst_1:
               comp_lst_1.append(word)
    if comp_lst_1 is []:
        return "nope"
    for actual_word in comp_lst_1:
        score = get_word_score(actual_word, HAND_SIZE)
        if score >max:
            max = get_word_score(actual_word, HAND_SIZE)
    for actual_words in comp_lst_1:
        word_score = get_word_score(actual_words, HAND_SIZE)
        if word_score == max:
            return actual_words


def comp_play_hand(hand, word_list):
    comp_word = ""
    total_score = 0
    while comp_word != "nope":
        display_hand(hand)
        comp_word=comp_choose_word(hand, word_list)
        if comp_word is None:
            print "Total Word Score:", total_score
            return total_score
        else:
            w_score = get_word_score(comp_word, word_list)
            total_score = w_score+total_score
            print comp_word
            print w_score
            hand=update_hand(hand, comp_word)


def get_easy_word(hand,word_list):
    comp_lst_1 = []
    max = 0
    for number in range (1, HAND_SIZE+1):
        words = get_perms(hand , number)
        for word in words:
            if is_valid_word(word, hand, word_list) is True and word not in comp_lst_1:
               comp_lst_1.append(word)
    if comp_lst_1 is []:
        return "nope"
    for actual_word in comp_lst_1:
        score = get_word_score(actual_word, HAND_SIZE)
        if score > max and score <= 15:
            max = get_word_score(actual_word, HAND_SIZE)
    for actual_words in comp_lst_1:
        word_score=get_word_score(actual_words, HAND_SIZE)
        if word_score == max:
            return actual_words


def play_com_easy(hand,word_list):
    comp_word = ""
    total_score = 0
    while comp_word != "nope":
        display_hand(hand)
        comp_word = get_easy_word(hand,word_list)
        if comp_word is None:
            print "Total Word Score:", total_score
            return total_score
        else:
            w_score = get_word_score(comp_word, word_list)
            total_score = w_score + total_score
            print comp_word
            print w_score
            hand = update_hand(hand, comp_word)


def get_medium_word(hand,word_list):
    comp_lst_1 = []
    max = 0
    for number in range(1, HAND_SIZE + 1):
        words = get_perms(hand, number)
        for word in words:
            if is_valid_word(word, hand, word_list) is True and word not in comp_lst_1:
                comp_lst_1.append(word)
    if comp_lst_1 is []:
        return "nope"
    for actual_word in comp_lst_1:
        score = get_word_score(actual_word, HAND_SIZE)
        if score > max and score <= 25:
            max = get_word_score(actual_word, HAND_SIZE)
    for actual_words in comp_lst_1:
        word_score = get_word_score(actual_words, HAND_SIZE)
        if word_score == max:
            return actual_words


def play_com_medium(hand, word_list):
    comp_word = ""
    total_score = 0
    while comp_word != "nope":
        display_hand(hand)
        comp_word = get_medium_word(hand, word_list)
        if comp_word is None:
            print "Total Word Score:", total_score
            return total_score
        else:
            w_score = get_word_score(comp_word, word_list)
            total_score = w_score + total_score
            print comp_word
            print w_score
            hand = update_hand(hand, comp_word)


def win (p_score, c_score):
    if p_score > c_score:
        print "Congratulations you beat the computer"
    elif c_score == p_score:
        print "Wow, you tied the computer. Good Job."
    elif p_score < c_score:
        print "Sorry, you lost. Better luck next time"


def com_difficulty(hand, word_list, difficulty):
    if difficulty == "easy":
        return play_com_easy(hand, word_list)
    elif difficulty == "medium":
        return play_com_medium(hand, word_list)
    elif difficulty == "hard":
        return comp_play_hand(hand, word_list)


def play_game(word_list):
    type = raw_input("Type 'u' to play alone or type 'c' to play against the computer: ")
    if type == "u":
        hand = deal_hand(HAND_SIZE)
        play_hand(hand, word_list)
        player_input = ""
        while player_input != "e":
            player_input = raw_input(
                "Type 'n' to to play a new hand, type 'r' to replay hand, or type 'e' to exit the game: ")
            if player_input == "e":
                print "Thanks for playing."
                type = raw_input("Type 'c' to play against the computer. Type 'e' to exit the the game: ")
                if type == "e":
                    quit()
            elif player_input == "r":
                play_hand(hand, word_list)
            elif player_input == "n":
                hand = deal_hand(HAND_SIZE)
                play_hand(hand, word_list)
    if type == "c":
        hand = deal_hand(HAND_SIZE)
        difficulty = raw_input("What difficulty DO YOU DESIRE(easy, medium or hard): ")
        difficulty = difficulty.lower()
        player_score = play_hand(hand, word_list)
        computer_score = com_difficulty(hand, word_list, difficulty)
        player_input = ""
        win(player_score, computer_score)
        while player_input != "e":
            player_input = raw_input("Type 'n' to to play a new hand, type 'r' to replay hand, or type 'e' to exit the game: ")
            if player_input == "e":
                print "Thanks for playing"
                quit()
            elif player_input == "r":
                difficulty = raw_input("What difficulty DO YOU DESIRE(easy, medium or hard): ")
                difficulty = difficulty.lower()
                player_score = play_hand(hand, word_list)
                computer_score = com_difficulty(hand, word_list, difficulty)
                win(player_score, computer_score)
            elif player_input == "n":
                hand = deal_hand(HAND_SIZE)
                difficulty = raw_input("What difficulty DO YOU DESIRE(easy, medium or hard): ")
                difficulty = difficulty.lower()
                player_score = play_hand(hand, word_list)
                computer_score = com_difficulty(hand, word_list, difficulty)
                win(player_score, computer_score)

if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)