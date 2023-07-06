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
    bet_message = input('何枚BETしますか？(1-99)')
    bet_coin = int(bet_message)
    print(bet_coin)

def play():
  print('デバッグログ：play()')
  
  human = Human('MY', 500)
  human.info()

  human.bet()

play()