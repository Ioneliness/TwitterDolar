import requests
import json
from Image import create_image
from twitter import api
import tweepy
from random import choice
import os
from time import sleep

url = requests.get('https://api.hgbrasil.com/finance?array_limit=1&key=1dbfaeb4')
jso = url.json()
dolar0 = (jso['results']['currencies']['USD']['buy'])
dolar1 = f'{dolar0:.2f}'
dolar2 = float(dolar1)
dolarformated = f'R${dolar2:.2f}'.replace('.',',')

list_emotes_sad = ['╥﹏╥','ಥ_ಥ','●︿●','ಠ╭╮ಠ','(ㄒoㄒ)','(Ｔ▽Ｔ)','(︶︹︺)','(┳◇┳)','(ToT)','(;﹏;)','(T＿T)','（´＿｀）','(T⌓T)','(╥_╥)','（；へ：）','（ｉДｉ）','(T_T)','(ಥ﹏ಥ)','(个_个)','(⋟﹏⋞)','(ノ﹏ヽ)','(┳Д┳)','༶ඬ༝ඬ༶','(‘A`)','（πーπ）','(つ﹏<。)','(◕︿◕✿)']
list_emote_happy = ['≧ω≦','(⊙ᗜ⊙)','โ๏∀๏ใ','(≧∀≦)','۹⌤_⌤۹','୧☉□☉୨','(⊙ꇴ⊙)','(´∀`)٩','(^ᴗ^)۶','(ﾉ･ｪ･)ﾉ','۹(ÒہÓ)۶','(≧∇≦*)','ʘ ͜ʖ ʘ','(ᗒᗨᗕ)','（・ｗ・）','б（＞ε＜）∂','(⌬̀⌄⌬́)','٩(θ‿θ)۶','ヽ(＾Д＾)ﾉ','(★^O^★)','（๑✧∀✧๑）','(*≧∀≦*)','(* >ω<)','۹(˒௰˓)','۶(๑>ᴗ<๑)','٩(●ᴗ●)۶']
list_speak = ['NyanNyan', 'Meow Meow', 'Nyan nyan nyan', 'Nyan', 'Yeaaah', 'YeahYeah', 'Yeah', 'Nhênhê', 'Whah']

def value():
    with open('Txts/dolar.txt', 'r') as file:
        return float(file.read().splitlines()[0])

def post_twitter():
    if value() < dolar2:
        valor = value()
        speak = choice(list_speak)
        emote = choice(list_emotes_sad)
        create_image(dolarformated)
        with open('Txts\dolar.txt', 'w') as file:
            file.write(dolar1)
            file.close
        api.update_with_media('atual.png', status=f'{speak}.. o dolar subiu para {dolarformated} {emote}')
    
    elif value() > dolar2:
        valor = value()
        speak = choice(list_speak)
        emote = choice(list_emote_happy)
        create_image(dolarformated)
        with open('Txts\dolar.txt', 'w') as file:
            file.write(dolar1)
            file.close
        api.update_with_media('atual.png', status=f'{speak}.. o dolar desceu para {dolarformated} {emote}')

if __name__ == "__main__":
    while True:
        post_twitter()
        sleep(1800)
