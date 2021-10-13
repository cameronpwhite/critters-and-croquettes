from camel import Camel
from donkey import Donkey
from duck import Duck
from fish import Fish
from frog import Frog
from goat import Goat
from insect import Insect
from lizard import Lizard
from llama import Llama
from newt import Newt
from pig import Pig
from snake import Snake
from spider import Spider
from toad import Toad
from turtle import Turtle

miss_fuzz = Llama("Miss Fuzz", "domestic llama", "morning")

mr_ears = Donkey("Mr. Ears","domestic donkey", "midday")

billy = Goat("Billy", "domestic goat", "afternoon")

curly = Pig("Curly", "domestic pig", "morning")

joe = Camel("Joe", "domestic camel", "midday")

banana_boat = Snake("Banana Boat", "domestic snake")

hop = Frog("Hop", "domestic frog")

webster = Spider("Webster", "domestic spider")

liz = Lizard("Liz", "domestic lizard")

sheldon = Turtle("Sheldon", "domestic turtle")

quack = Duck("Quack", "domestic duck")

glub = Fish("Glub", "domestic fish")

leggy = Insect("Leggy", "domestic insect")

isaac = Newt("Isaac", "domestic newt")

mr_toad = Toad("Mr. Toad", "domestic toad")

roberto = Llama("Roberto", "alpaca", "midday")

print(f'{roberto.name} the {roberto.species} is available during the {roberto.shift} shift.')

