import requests
import cv2 as cv
import os
import matplotlib.pyplot as plt
import numpy as np
import random

marks = ['ハート','スペード','ダイヤ','クローバー']
display_names = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
numbers = [1,2,3,4,5,6,7,8,9,10,10,10,10]

def load_image():
  global card_images
  image_name = 'cards.jpg'
  vsplit_number = 4
  hsplit_number = 13
  
  if not os.path.isfile(image_name):
    response = requests.get('http://3156.bz/techgym/cards.jpg', allow_redirects=False)
    with open(image_name, 'wb') as image:
      image.write(response.content)
   
  img = cv.imread('./cards.jpg')
  img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
 
  h, w = img.shape[:2]
  crop_img = img[:h // vsplit_number * vsplit_number, :w // hsplit_number * hsplit_number]
  
  card_images = []
  for h_image in np.vsplit(crop_img, vsplit_number):
    for v_image in np.hsplit(h_image, hsplit_number):
      card_images.append(v_image)
  card_images = np.array(card_images)



class Player:
  def __init__(self, name):
    self.name = name

class Human(Player):
  def __init__(self, name, coin):
    super().__init__(name)
    self.coin = coin

  def show_coin(self):
    print(f"現在の持ちコインは{self.coin}コインです")

  def set_bet_coin(self, bet_coin):
    self.coin -= bet_coin
    print(f"BETしたコインは{bet_coin}コインです")

  def bet(self):
    if self.coin >= 100:
      max_bet_coin = 100
    else:
      max_bet_coin = self.coin
    bet_message = (f"何枚BETしますか？：(1-{max_bet_coin})")
    bet_coin = input(bet_message)
    while not self.enable_bet_coin(bet_coin, max_bet_coin):
      bet_coin = input(bet_message)
    self.set_bet_coin(int(bet_coin))

  def enable_bet_coin(self, string, max_bet_coin):
    if string.isdigit():
      number = int(string)
      if number >= 10 and number <= max_bet_coin:
        return True
      else:
        return False
    else:
      return False

class Computer(Player):
  def __init__(self, name):
    super().__init__(name)