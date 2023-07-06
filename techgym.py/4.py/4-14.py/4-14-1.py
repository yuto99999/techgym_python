import random

players = []
tables = []

class Player:
  def __init__(self, name, coin):
    self.name = name
    self.coin = coin

  def info(self):
    print(self.name + '：' + str(self.coin))

  def set_bet_coin(self, bet_coin):
    self.coin -= bet_coin
    print(self.name + 'は ' + str(bet_coin) + 'コイン BETしました。')

class Human(Player):
  def __init__(self, name, coin):
    super().__init__(name, coin)

  def bet(self):
    bet_message = '何枚BETしますか？：(1-99)'
    bet_coin = input(bet_message)
    while not self.enable_bet_coin(bet_coin):
      bet_coin = input(bet_message)
    super().set_bet_coin(int(bet_coin))

  def enable_bet_coin(self, string):
    if string.isdigit():
      number = int(string)
      if number >= 1 and number <= 99:
        return True
      else:
        return False
    else:
      return False

class Computer(Player):
  def __init__(self, name, coin):
    super().__init__(name, coin)

  def bet(self):
    if self.coin >= 99:
      max_bet_coin = 99
    else:
      max_bet_coin = self.coin
    bet_coin = random.randint(1, max_bet_coin)
    super().set_bet_coin(bet_coin)

class Cell:
  def __init__(self, name, rate, color):
    self.name = name
    self.rate = rate
    self.color = color

def create_players():
  global players
  human = Human('MY', 500)
  computer1 = Computer('C1', 500)
  computer2 = Computer('C2', 500)
  computer3 = Computer('C3', 500)
  players = [human, computer1, computer2, computer3]

def show_players():
  for player in players:
    player.info()
  
  for player in players:
    player.bet()
 
  for player in players:
    player.info()

def create_table():
  global tables
  t1 = Cell('R', 8, 'red')
  t2 = Cell('B', 8, 'black')
  t3 = Cell('1', 2, 'red')
  t4 = Cell('2', 2, 'black')
  t5 = Cell('3', 2, 'red')
  t6 = Cell('4', 2, 'black')
  t7 = Cell('5', 2, 'red')
  t8 = Cell('6', 2, 'black')
  t9 = Cell('7', 2, 'red')
  t10 = Cell('8', 2, 'black')
  tables = [t1, t2, t3, t4, t5, t6, t7, t8, t9 ,t10]
  
def show_table():
  for table in tables:
    print('| ' + table.name + '(x' + str(table.rate) + ') |')

def play():
  print('デバッグログ：play()')
  create_table()
  show_table()
      
play()