import random
import math

teams = []
playing_teams = {'myself':False, 'enemy':False}
#Falseは空の状態を表していて、これから何かが入るよというコードを見る人に先に推測させるもので、深い意味はない

class Team:
    def __init__(self, name, attack, defense):
      self.name = name
      self.attack = attack
      self.defense = defense
      self.total_score = 0

    def info(self):
      print(f"{self.name}: 攻撃力:{self.attack}/ 守備力:{self.defense}")
    
    def get_hit_rate(self):
       return random.randint(10, self.attack)
    
    def get_out_rate(self):
       return random.randint(10, self.defense)
    
def create_teams():
   global teams
   team1 = Team('アタッカーズ', 80, 20)
   team2 = Team('ディフェンダーズ', 30, 70)
   team3 = Team('アベレージーズ', 50, 50)
   teams = [team1, team2, team3]
  
def show_teams():
   index = 1
   print('全チームの情報')
   for team in teams:
      print(str(index))
      team.info()
      index += 1

def choice_team(player):
   if player == 'myself':
      player_name = '自分'
   elif player == 'enemy':
      player_name = '相手'
    
   choice_team_number = int(input(player_name + 'のチームを選択してください(1～3)'))
   playing_teams[player] = teams[choice_team_number - 1]
   print('{} のチームは「{}」です'.format(player_name, playing_teams[player].name))
  
def get_play_inning(inning):
   if inning == 'front':
      hit_rate = playing_teams['myself'].get_hit_rate()
      out_rate = playing_teams['enemy'].get_out_rate()
   elif inning == 'back':
      hit_rate = playing_teams['enemy'].get_hit_rate()
      out_rate = playing_teams['myself'].get_out_rate()
    
   inning_score = math.floor((hit_rate - out_rate) / 10)
   if inning_score < 0:
      return 0
   return inning_score

def play():
   create_teams()
   show_teams()
   choice_team('myself')
   choice_team('enemy')
   score_borads = ['＿＿｜','自分｜','相手｜']
   for i in range(9):
      score_borads[0] += str(i + 1) + '｜'

      inning_score = get_play_inning('front')
      score_borads[1] += str(inning_score) + '｜'
      playing_teams['myself'].total_score += inning_score

      if i == 8 and playing_teams['myself'].total_score < playing_teams['enemy'].total_score:
         score_borads[2] += 'X｜'
      else:
         inning_score = get_play_inning('back')
         score_borads[2] += str(inning_score) + '｜'
         playing_teams['enemy'].total_score += inning_score
   score_borads[0] += 'R｜'
   score_borads[1] += str(playing_teams['myself'].total_score) + '｜'
   score_borads[2] += str(playing_teams['enemy'].total_score) + '｜'
   print(score_borads[0])
   print(score_borads[1])
   print(score_borads[2])

play()
                          