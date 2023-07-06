import random

data = [['見','貝'], ['土','士'], ['眠','眼']]
level = 1

def start_message():
  print('違う漢字の番号(例:A1)を入力してください')

def section_message():
  print('レベル:' + str(level))

def view_question():
  choice_data = random.randint(0, 2)
  mistake_number = random.randint(0, 8)
  print('デバッグ:mistake_number = ' + str(mistake_number))
  question = data[choice_data]
  print(question)
  i = 0
  j = 0
  print('／｜A B C')
  print('ーーーーー')
  while i < 3:
    question_str = str(i + 1) + '｜'
    while j < 3:
      if (i * 3 + j) == mistake_number:
        question_str += question[1]
      else:
        question_str += question[0]
      j += 1
    print(question_str)
    i += 1
    j = 0

def change_input_numebr(input_str):
  str_data = {'A':0, 'B':1, 'C':2}
  input_str_split = list(input_str)
  col_number = str_data[input_str_split[0]]
  row_number = int(input_str_split[1]) - 1
  input_numebr = col_number + row_number * 3
  return input_numebr

def play():
  section_message()
  view_question()
  choice = input('(例:A1)')
  print('デバッグ:choice = ' + choice)
  input_number = change_input_numebr(choice)
  print('デバッグ:input_number = ' + str(input_number))

start_message()
play()