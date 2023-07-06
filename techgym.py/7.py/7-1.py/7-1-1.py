import random

hands = ['グー', 'チョキ', 'パー']
results = {'win':'勝ち', 'lose':'負け', 'draw':'あいこ'}
players = []

class Player:
  def __init__(self, name, life):
    self.name = name
    self.life = life

def create_players():
  players.append(Player('自分', 3))
  players.append(Player('相手', 3))

def start_message():
  print('じゃんけんスタート')

def life_mesage():
  print(f"ライフ {players[0].name}:{players[0].life} / {players[1].name}:{players[1].life}")

def is_hand(string):
  if string.isdigit():
    number = int(string)
    if number >= 0 and number <= 2:
      return True
    else:
      return False
  else:
    return False

def get_my_hand():
  print(f"{players[0].name}の手を入力してください")
  input_message = ''
  index = 0
  for hand in hands:
    input_message += str(index) + ':' + hand
    if index < 2:
      input_message += ', '
    index += 1
  return input(input_message)

def get_you_hand():
  return random.randint(0, 2)

def get_hand_name(hand_number):
  return hands[hand_number]

def view_hand(my_hand, you_hand):
  print(f"{players[0].name}の手は{get_hand_name(my_hand)}")
  print(f"{players[1].name}の手は{get_hand_name(you_hand)}")

def get_result(hand_diff):
  if hand_diff == 0:
    return 'draw'
  elif hand_diff == -1 or hand_diff == 2:
    return 'win'
  else:
    return 'lose'

def view_result(result):
  print(results[result])

def change_life(result):
  if result == 'win':
    players[1].life -= 1
  elif result == 'lose':
    players[0].life -= 1

def is_game_end():
  for player in players:
    if player.life == 0:
      return True
    else:
      return False

def play():
  create_players()
  life_mesage()
  my_hand = get_my_hand()
  while not is_hand(my_hand):
    my_hand = get_my_hand()

  my_hand = int(my_hand)
  you_hand = get_you_hand()
  hand_diff = my_hand - you_hand

  view_hand(my_hand, you_hand)
  result = get_result(hand_diff)
  view_result(result)
  change_life(result)
  while not is_game_end():
    play()

start_message()
play()
life_mesage()
