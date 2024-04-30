#importing library 
import random 

#storing the signs and the rank value 
cards = ["♦️", "♠️", "♥️", "♣️"] 
ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"] 

#random value from both the list and return the value 
def pick_a_card(): 
	card = random.choices(cards) 
	rank = random.choices(ranks) 
	
	# returning the selected card 
	return(f"The {rank} of {card}") 

# printing the selected card 
print(pick_a_card())
