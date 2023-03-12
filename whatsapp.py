import random
import pyautogui as pg
import time

flower=["rose","lotus","]
time.sleep(1)
for i in range(10):
	a=random.choice(flower)
	pg.write("You are my "+a)
	pg.press('enter')