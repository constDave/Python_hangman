import random

# make a list of words
words = [
	'apple', 
	'blueberry',
	'orange', 
	'lemon', 
	'melon', 
	'grapefruit',
	'lime',
	'jicama'
]

while True:
	start = input("Press enter/return to start, or enter Q to quit")
	if start.lower() == 'q':
		break
	# pick a random word
	secret_word = random.choice(words)
	bad_guesses = []
	good_guesses = []

	while len(bad_guesses) < 7 and len(good_guesses) != len(list(secret_word)):
		# draw spaces
		# draw guessed letters and strikes
		for letter in secret_word:
			if letter in good_guesses:
				print(letter, end='')
			else:
				print('_',end='')
		print('')		
		print("Strikes: {}/7".format(len(bad_guesses)))
		print(" ")
	# take a guess
		guess = input("Guess a letter: ").lower()
		if len(guess) != 1:
			print("You can only guess a single letter!")
			continue
		elif guess in bad_guesses or guess in good_guesses:
			print("You've already guessed that letter..")	
		elif not guess.isalpha():
			print("You can only guess letters!")	
			continue
		
		if guess in secret_word:
			good_guesses.append(guess)	
			if len(good_guesses) == len(list(secret_word)):
				print("You Win! The word was {}".format(secret_word))
				break
		else:
			bad_guesses.append(guess)
	else:
		print("You didn't guess it! My secret word was {}".format(secret_word))	