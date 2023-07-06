import random

players = []

class Player:
  def __init__(self, name, coin):
    self.name = name
    self.coin = coin

  def info(self):
    print(self.name + '：' + str(self.coin))

  def set_bet_coin(self, bet_coin):
    self.coin -= bet_coin

class Human(Player):
  def __init__(self, name, coin):
    super().__init__(name, coin)

  def bet(self):
    bet_message = '何枚BETしますか？：(1-99)'
    bet_coin = input(bet_message)
    while not self.enable_bet_coin(bet_coin):
      bet_coin = input(bet_message)
    super().set_bet_coin(int(bet_coin))
    print(bet_coin)

  def enable_bet_coin(self, string):
    if string.isdigit():
      number = int(string)
      if number >= 1 and number <= 99:
        return True
      else:
        return False
    else:
      return False

def create_players():
  global players
  human = Player('MY', 500)
  com1 = Computer('C1', 500)
  com2 = Computer('C2', 500)
  com3 = Computer('C3', 500)
  players = [human, com1, com2, com3]

def play():
  print('デバッグログ：play()')
  create_players()
  
class Computer(Player):
  def __init__(self, name, coin):
    super().__init__(name, coin)

play()