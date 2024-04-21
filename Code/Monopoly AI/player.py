#!/usr/bin/env python3

from time import sleep
import random
import game_board

# The Player class simulates a Monopoly player who randomly decides what to do each turn
# for the Agent to play against to learn.
class Player:
	# Initialization.
	def __init__(self, player_num):
		self.states = ["inactive", "buying", "chance/community chest", "collecting money from bank", "paying money to bank", "collecting rent", "paying rent", "in jail"]
		self.player = {"position": 0, "properties": [], "houses": {}, "hotels": {}, "cards": [], "money": 1500, "state": self.states[0], "is_bankrupt": True}
		self.colour_set = {"brown": 0, "light_blue": 0, "purple": 0, "orange": 0, "red": 0, "yellow": 0, "green": 0, "blue": 0}
		self.colour_num = {"brown": 2, "light_blue": 3, "purple": 3, "orange": 3, "red": 3, "yellow": 3, "green": 3, "blue": 2}
		self.player_num = player_num
		
		# Houses and hotels.
		for i in game_board.game:
			self.player["houses"][i] = 0
			self.player["hotels"][i] = 0
	
	# Check if the player is in Jail
	def is_in_jail(self):
		if self.player["position"] == 30:
			self.player["position"] = game_board.game["Jail"]["position"]
			self.player["money"] -= 50
			self.player["state"] = self.states[8]
			return True
		else:
			return False
	
	# Roll dice on call (turn).
	def roll_dice(self):
		new_pos = [rnd.randint(1, 6), rnd.randint(1, 6)]
		doubles = 0
		while new_pos[0] == new_pos[1] or new_pos[1] == new_pos[0]:
			doubles += 1
			new_pos = [rnd.randint(1, 6), rnd.randint(1, 6)]
			if doubles >= 3:
				self.player["position"] = 30
				self.is_in_jail()
		self.player["position"] += new_pos[0] + new_pos[1]
		if self.player["position"] > 39:
			self.player["position"] = 0 + (self.player["position"] - 39)
	
	# Buy property on input position and append it to the 'self.player' variable's "properties"
	# key.
	def buy_property(self, position):
		for i in game_board.game:
			if game_board.game[i]["position"] == position and game_board[i]["type"] == "property":
				self.player["state"] = self.states[1]
				self.player["properties"].append(i)
				self.player["money"] -= game_board.game[i]["price"]
				if game_board.game[i]["color"] != "railroad" or game_board.game[i]["color"] != "utility":
					self.colour_set[game_board.game[i]["color"]] += 1
				self.player["state"] = self.states[0]
			else:
				break
	
	# Buy houses or hotels on owned properties
	def buy_house_hotel(property):
		if not property in self.player["properties"]:
			return None
		else:
			if self.colour_set[game_board.game[property]["color"]] == self.color_num[game_board.game[property]["color"]]:
				if self.player["houses"][property] == 4:
					if self.player["hotels"] == 1:
						return None
					else:
						self.player["money"] -= 200
						self.player["hotels"] += 1
				else:
					self.player["money"] -= 100
					self.player["houses"][property] += 1
			else:
				return None
		
		# Randomly decide if the player should buy a building. However, the PLayer will not
		# buy the building if it is too much money for it to buy (1000 less than the total
		# monetary value of the player)
		def is_buying_building(self):
			for i in game_board.game:
				if game_board.game[i]["type"] == "property" and self.player["position"] == game_board.game[i]["position"]:
					if game_board.game[i]["price"] <= self.player["money"] - 1000:
						is_buying = bool(rnd.randint(0, 1))
						if is_buying:
							if not i in self.player["properties"]:
								self.buy_property(self.player["position"])
							else:
								if game_board.game[i]["color"] != "railroad" or game_board.game[i]["color"] != "utility":
									buy_house_hotel(i)
								else:
									break
						else:
							break
				break
		
		# Check if the position it is on is owned by someone. If so, return a boolean that will trigger
		# a rent function in the game loop.
		def is_pay_rent(self, property, player):
			check_for_rent = False
			for i in game_board.game:
				if game_board.game[i]["position"] == self.player["position"] and game_board.game[i]["type"] == "property":
					rent = game_board.game[i]["rent"][0]
					if player.player["houses"][property] != 0:
						rent = game_board.game[i]["rent"][0] * self.player["houses"][property]
					elif player.player["hotels"][property] != 0:
						rent = game_board.game[i]["rent"][0] * 4
					if game_board.game[i]["is_owned"]:
						self.player["money"] -= rent
						player["money"] += rent
		
		# Handles community chest and chance cards. For simplification, you either gain or loose an amount 
		# of money equivalent to a random number between 20 and 100
		def chance_community_cards(self):
			for i in game_board.game:
				if game_board.game[i]["position"] == self.player["position"]:
					if game_board.game[i]["type"] == "chance" or game_board.game[i]["type"] == "community_chest":
						is_gaining_money = bool(random.randint(0, 1))
						if is_gaining_money:
							self.player["money"] += random.randint(20, 100)
						else:
							self.player["money"] -= random.randint(20, 100)
			
		# Final turn function.
		def turn(self, players):
			self.roll_dice()
			self.is_in_jail()
			if self.player["state"] == "in jail":
				return None
			self.chance_community_card()
			property = ""
			i = 0
			for i in game_board.game:
				if game_board.game[i]["position"] == self.player["position"] and game_board.game[i]["type"] == "property":
					property = i
					for player in players:
						for j in player.player["properties"]:
							if j == property:
								self.is_pay_rent(property, player)
								break
							else:
								i += 1
						if i >= len(players):
							self.is_buying_building()
							break