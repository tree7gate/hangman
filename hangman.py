from random import choice
# from IPython.display import clear_output

class Hangman():

	def __init__(self):
		self.animals = ['monkey', 'hippopotamus', 'turtle', 'panda', 'alligator', 'cheetah']
		self.sports = ['gymnast', 'archery', 'basketball', 'dodgeball', 'surfing', 'football']
		self.lives = len(choice(self.sports))
		self.letter_list = []
		
	def pickCategory(self):
		ans = input('Choose a category: animals or sports ')
		try:
			if ans.lower() == 'animals':
				return self.animals
			else:
				return self.sports
		except:
			print('type "animals" or "sports"')
		

	def askInput(self):
		ans = input('Enter a letter: ')
		return ans

	def chooseWord(self, lst):
		return choice(lst)


	def hideLetter(self, word):
		hidden_word = ['_' for letter in word]
		return ' '.join(hidden_word)

	def separateLetter(self, word):
		return [(word[i], i) for i in range(len(word))]

	def showLetter(self, letter, lst, hidden_word):
		check_list = [item[0] for item in lst]
		
		# turn string hidden_word into list and strip whitespaces
		hidden_list = list(hidden_word.replace(' ', ''))
		for ele in lst:
			if letter == ele[0]:
				hidden_list[ele[1]] = letter
										
		if letter not in check_list:
			self.lives -= 1
		return ' '.join(hidden_list)


	def letterList(self, letter):
		if letter not in self.letter_list:
			self.letter_list.append(letter)
		else:
			print('You have already entered the letter!')

my_game = Hangman()

while True:

	word_list = my_game.pickCategory()
	word = my_game.chooseWord(word_list)
	# word = 'hippopotamus'
	hide = my_game.hideLetter(word)
	lst = my_game.separateLetter(word)
	# print(lst)
	# print('Lives: {}'.format(my_game.counter(word)))
	# print(hide)
	
	while True:
		
		print('Lives: {}'.format(my_game.lives))
		print(hide)

		letter = my_game.askInput()
		
		hide = my_game.showLetter(letter, lst, hide)
		my_game.letterList(letter)
		# print(lst)
		if word == hide.replace(' ', ''):
			print(hide)
			print('you won!')
			break
		elif my_game.lives == 0:
			print('WoW, you actually lost!')
			break
		else:
			continue

	ans = input('Would you like to play again? ')
	if ans.lower() == 'no':
		break






