import random

class Player:
  def __init__(self, name, coin):
    self.name = name
    self.coin = coin

  def info(self):
    print(self.name + '：' + str(self.coin))

class Human(Player):
  def __init__(self, name, coin):
    super().__init__(name, coin)

  def bet(self):
    bet_messaage = '何枚BETしますか？：(1-99)'
    bet_coin = input(bet_messaage)
    while not self.enable_bet_coin(bet_coin):
      bet_coin = input(bet_messaage)
    print(bet_coin)

  def enable_bet_coin(self, string):
    if string.isdigit():
      number = int(string)
      if number >= 0 and number <= 99:
        return True
      else:
        return False
    else:
      return False

def play():
  print('デバッグログ：play()')
  
  human = Human('MY', 500)
  human.info()

  human.bet()

play()