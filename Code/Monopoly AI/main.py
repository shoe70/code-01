#!/usr/bin/env python3

import player
import agent
import game_board
import random
import math

# NOTE - For the sake of simplicity, auctioning is not executed.

class Game:
	# Initialization.
	def __init__(self, epochs):
		self.heuristics = {}
		self.misc = ["Community Chest", "Chance", "Income Tax", "Super Tax", "Go To Jail", "Jail", "Just Visiting", "Go", "Free Parking"]
		self.utilities = ["Kings Cross Station", "Electric Company", "Marylebone Station", "Fenchurch St. Station", "Water Works", "Liverpool St. Station"]
		self.players = [player.Player(0)]
		self.end_game = 0
		self.is_game_end = False
		self.epochs = epochs
		
	# Find the percentage of rent compared to the price. This evaluates the amount of points the
	# AI recieves to be used in RL (Reinforcement Learning).
	def evaluate_heuristics(self):
		for property in game_board.game:
			self.heuristics[property] = []
			# Properties (e.g Mayfair)
			if game_board.game[property]["type"] == "property" and game_board.game[property]["color"] != "railroad" and game_board.game[property]["color"] != "utility":
				for rent in game_board.game[property]["rent"]:
					percentage = rent / game_board.game[property]["price"] * 100
					self.heuristics[property].append(round(percentage, 2))
			# Stations (e.g Kings Cross St.)
			elif game_board.game[property]["type"] == "property" and game_board.game[property]["color"] == "railroad":
				for rent in game_board.game[property]["rent"]:
					self.heuristics[property].append(math.trunc(rent / 2))
			elif game_board.game[property]["type"] == "property" and game_board.game[property]["color"] == "utility":
				self.heuristics[property].append(0.1)
				self.heuristics[property].append(0.2)
		return self.heuristics
	
	def play_game():
		i = 0
		while i < self.epochs:
			if self.is_game_end:
				i += 1
				
game = Game(1)
heuristics = game.evaluate_heuristics()
print(heuristics)