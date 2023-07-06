import random
import math

data = [['m ','n '], ['l ','I '],['F ','E ']]
number_data = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
level = 1
col = 3
row = 3

def start_message():
    print('マチガイ探し')

def section_message():
    print(f"レベル:{level}")

def view_question():
    choice_data_number = random.randint(0, 2)
    mistake_number = random.randint(0, (col * row) - 1)
    question = data[choice_data_number]
    print(question)
    i = 0
    j = 0
    question_str1 = '／｜'
    question_str2 = 'ーー'
    while i < col:
        question_str1 += number_data[i] + ' '
        question_str2 += 'ー'
        i += 1
    print(question_str1)
    print(question_str2)
    i = 0
    while i < row:
        question_str = str(i + 1) + ' | '
        while j < col:
            if mistake_number == (i * col + j):
                question_str += question[1]
            else:
                question_str += question[0]
            j += 1
        i += 1
        j = 0
        print(question_str)
    return mistake_number

def change_input_str(input_str):
    str_data = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7, 'I':8}
    input_str_split = list(input_str)
    col_number = str_data[input_str_split[0]]
    row_number = int(input_str_split[1]) - 1
    input_number = col_number + row_number * col
    return input_number

def is_correct_number(mistake_number, input_number):
    if mistake_number == input_number:
        return True
    else:
        return False

def view_result(is_correct, mistake_number):
    if is_correct:
        print('正解！')
        if level < 13:
            level_up()
            play()
    else:
        print('不正解')
        print(f"正解は{change_number(mistake_number)}")

def change_number(number):
    col_number = number % col
    row_number = math.floor(number / col) + 1
    correct_number = number_data[col_number] + str(row_number)
    return correct_number

def level_up():
    global level, col, row
    level += 1
    if level % 2 == 0:
        col += 1
    else:
        row += 1


def play():
    section_message()
    mistake_number = view_question()
    choice = input('(例:A1)')
    input_number = change_input_str(choice)
    is_correct = is_correct_number(mistake_number, input_number)
    view_result(is_correct, mistake_number)
    

start_message()
play()