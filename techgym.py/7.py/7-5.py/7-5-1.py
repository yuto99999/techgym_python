import random
import math

players = []
playing_teams = {'myself':False, 'enemy':False}

class Team:
    def __init__(self, id, name, attack, defense):
        self.id = id
        self.name = name 
        self.attack = attack
        self.defense = defense
        self.total_score = 0
    
    def info(self):
        print(f"{self.name}:攻撃力:{self.attack}/守備力{self.defense}")
    
    def get_hit_rate(self):
        return random.randint(10, self.attack)
    
    def get_out_rate(self):
        return random.randint(10, self.defense)

def create_players():
    global players
    players.append(Team(1,'アタッカーズ',80 ,20))
    players.append(Team(2,'ディフェンダーズ',30 ,70))
    players.append(Team(3,'アベレージーズ',50 ,50))

def show_players():
    print('全チームの情報')
    for i, player in enumerate(players):
        print(f"{i + 1}")
        player.info()

def choice_team(player):
    if player == 'myself':
        player_name = '自分'
    elif player == 'enemy':
        player_name = '相手'
    
    message = (f"{player_name}のチームを選択してください")
    choice_team_number = input(message)
    while not enable_choice(choice_team_number, player):
        choice_team_number = input(message)
    playing_teams[player] = players[int(choice_team_number) - 1]
    print(f"{player_name}のチームは「{playing_teams[player].name}」です")

def enable_choice(string, player):
    if string.isdigit():
        number = int(string)
        if number >= 1 and number <= 3:
            if player == 'enemy':
                if number == playing_teams['myself'].id:
                    return False
            return True
        else:
            return False
    else:
        return False

def get_inning_score(inning):
    if inning == 'front':
        hit_rate = playing_teams['myself'].get_hit_rate()
        out_rate = playing_teams['enemy'].get_out_rate()
    elif inning == 'back':
        hit_rate = playing_teams['enemy'].get_hit_rate()
        out_rate = playing_teams['myself'].get_out_rate()
    inning_score = math.floor((hit_rate - out_rate) / 10)
    if inning_score <= 0:
        inning_score = 0
    return inning_score

def play():
    create_players()
    show_players()
    choice_team('myself')
    choice_team('enemy')
    score_boards = ['＿＿｜', '自分｜', '相手｜']
    for i in range(9):
        score_boards[0] += str(i + 1) + '｜'

        inning_score = get_inning_score('front')
        score_boards[1] += str(inning_score) + '｜'
        playing_teams['myself'].total_score += inning_score

        if i == 8 and playing_teams['myself'].total_score < playing_teams['enemy'].total_score:
            score_boards[2] += 'X｜'
        else:
            inning_score = get_inning_score('back')
            score_boards[2] += str(inning_score) + '｜'
            playing_teams['enemy'].total_score += inning_score
    score_boards[0] += 'R｜'
    score_boards[1] += str(playing_teams['myself'].total_score) + '｜'
    score_boards[2] += str(playing_teams['enemy'].total_score) + '｜'
    print(score_boards[0])
    print(score_boards[1])
    print(score_boards[2])

play()