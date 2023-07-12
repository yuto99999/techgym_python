import random

hands = ['グー','チョキ','パー']
results = {'win':'勝ち', 'lose':'負け', 'draw':'あいこ'}
lifes = {'my':3, 'you':3}

def start_message():
  print('じゃんけんスタート')

def initialize():
  global lifes
  lifes = {'my':3, 'you':3}

def show_lifes():
  print(f"ライフ 自分:{lifes['my']} / 相手:{lifes['you']}")

def get_my_hand():
  print('自分の手を入力してください')
  index = 0
  input_message = ''
  for hand in hands:
    input_message += str(index) + ':' + hand
    if index < 2:
      input_message += ','
    index += 1
  return input(input_message)

def is_hand(string):
  if string.isdigit():
    number = int(string)
    if number >= 0 and number <= 2:
      return True
    else:
      return False
  else:
    return False

def get_you_hand():
  return random.randint(0, 2)

def get_hand_name(hand_number):
  return hands[hand_number]

def view_hand(my_hand, you_hand):
  print(f"自分の手は{get_hand_name(my_hand)}")
  print(f"相手の手は{get_hand_name(you_hand)}")

def get_result(hand_diff):
  if hand_diff == 0:
    return 'draw'
  elif hand_diff == -1 or hand_diff == 2:
    return 'win'
  else:
    return 'lose'

def view_result(result):
  print(results[result])
  show_lifes()

def update_lifes(result):
  if result == 'lose':
    lifes['my'] -= 1
  elif result == 'win':
    lifes['you'] -= 1

def get_replay():
  message = '再戦しますか？:(Y or N)'
  replay = input(message)
  while not enable_replay(replay):
    replay = input(message)
  if replay == 'Y':
    return True
  else:
    return False

def enable_replay(string):
  if string == 'Y' or string == 'N':
    return True
  else:
    return False

def play_once():
  my_hand = get_my_hand()
  while not is_hand(my_hand):
    my_hand = get_my_hand()
  my_hand = int(my_hand)
  you_hand = get_you_hand()
  hand_diff = my_hand - you_hand
  view_hand(my_hand, you_hand)
  result = get_result(hand_diff)
  update_lifes(result)
  view_result(result)
  if lifes['my'] > 0 and lifes['you'] > 0:
    play_once()
  else:
    if get_replay():
      play()

def play():
  initialize()
  show_lifes()
  play_once()

play()

