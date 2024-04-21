#!/usr/bin/env python3

import numpy as np
import game_board

# The Agent class generates a biased mean on each turn, determining the probability that the AI will buy the property.
# It determines the mean by taking in the price of the houses and hotels and checking the price of the colour set
# (determining the probability that the AI will max the property (houses, hotels etc.)). It then uses
class Agent():
	def __init__(self, agent_num, heuristics):
		self.states = ["inactive", "buying", "chance/community chest", "collecting money from bank", "paying money to bank", "collecting rent", "paying rent", "in jail"]
		self.agent = {"position": 3, "properties": [], "cards": [], "money": 1500, "state": self.states[0]}
		self.agent_num = agent_num
		# Variables for neural network...
		self.heuristics = heuristics
		# seed random numbers to make calculation deterministic.
		np.random.seed(1)
		
	# This function loops through each key in the heuristics dictionary and determines the weight of each
	# number in the array (corresponding to rent. This weight is determined by the total monetary value of the
	# agent (determines the probability of getting 1, 2, 3, 4... houses or a hotel) and uses those weights
	# to determine a biased mean.
	def calculate_mean(self, arr, property, x, y, epochs):
		weights = np.random.random(len(arr))
		# For simplification, houses are priced at 100m and hotels are priced at 200m.
		houses = [100, 50, 200, x]	# [prices, array for number of houses]
		hotels = [200, 100, 300, y]	# [prices, array for number of hotels]
		
	def check_and_calculate(self, houses, hotels):
		for i in self.heuristics:
			calculate_mean(self.heuristics[i], i, houses, hotels, 100)
	
	def roll_dice(self):
		new_pos = [random.randint(1, 6), random.randint(1, 6)]
		doubles = 0
		while new_pos[0] == new_pos[1] or new_pos[1] == new_pos[0]:
			doubles += 1
			new_pos = [random.randint(1, 6), random.randint(1, 6)]
			self.agent["state"] = self.states[8] if doubles >= 3 else None
		self.agent["position"] += new_pos[0] + new_pos[1]
		if self.agent["position"] > 39:
			self.agent["position"] = 0 + (self.agent["position"] - 39)

agent = Agent(0, {'Go': [], 'Old Kent Road': [0.01, 0.03, 0.1, 0.2, 0.4, 0.8], 'Community Chest': [], 'Whitechapel Road': [0.01, 0.07, 0.2, 0.6, 1.0, 1.4], 'Income Tax': [], 'Kings Cross Station': [0.12, 0.25, 0.5, 1.0], 'The Angel Islington': [0.01, 0.06, 0.18, 0.4, 0.8, 1.0], 'Chance': [], 'Euston Road': [0.01, 0.06, 0.18, 0.4, 0.8, 1.0], 'Pentonville Road': [0.01, 0.07, 0.17, 0.4, 0.6, 1.0], 'Just Visiting': [], 'Jail': [], 'Pall Mall': [0.01, 0.07, 0.2, 0.6, 0.8, 1.0], 'Electric Company': [0.1, 0.2], 'Whitehall': [0.01, 0.07, 0.2, 0.6, 0.8, 1.0], 'Northumberland Avenue': [0.01, 0.07, 0.2, 0.6, 0.8, 1.0], 'Marylebone Station': [0.12, 0.25, 0.5, 1.0], 'Bow Street': [0.02, 0.08, 0.2, 0.6, 0.8, 1.0], 'Marlborough Street': [0.02, 0.08, 0.2, 0.6, 0.8, 1.0], 'Vine Street': [0.02, 0.08, 0.2, 0.6, 0.8, 1.0], 'Free Parking': [], 'Strand': [0.02, 0.08, 0.2, 0.6, 0.6, 0.8], 'Fleet Street': [0.02, 0.08, 0.2, 0.6, 0.6, 0.8], 'Trafalgar Square': [0.02, 0.08, 0.2, 0.6, 0.6, 0.8], 'Fenchurch St. Station': [0.12, 0.25, 0.5, 1.0], 'Leicester Square': [0.02, 0.08, 0.2, 0.6, 0.6, 0.8], 'Coventry Street': [0.02, 0.08, 0.2, 0.6, 0.6, 0.8], 'Water Works': [0.1, 0.2], 'Piccadilly': [0.02, 0.09, 0.2, 0.6, 0.6, 0.8], 'Go To Jail': [], 'Regent Street': [0.02, 0.09, 0.2, 0.6, 0.6, 0.8], 'Oxford Street': [0.02, 0.09, 0.2, 0.6, 0.6, 0.8], 'Bond Street': [0.02, 0.09, 0.2, 0.6, 0.6, 0.8], 'Liverpool St. Station': [0.12, 0.25, 0.5, 1.0], 'Park Lane': [0.02, 0.1, 0.2, 0.6, 0.6, 0.8], 'Super Tax': [], 'Mayfair': [0.03, 0.1, 0.2, 0.6, 0.8, 1.0]})