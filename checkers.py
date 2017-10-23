import weechat

description = "Play checkers with your friends";

weechat.register("Checkers", "Ergot", "VERSION", "LICENSE", description, "", "")
weechat.hook_command("checkers", "Start a game of checkers", "", "", "", "startCheckers", "")
weechat.hook_signal("weechat_print", "checkCheckersInput", "")

# Board states
# ------------
# 0: Empty
# 1: Black
# 2: White
# 3: Black king
# 4: White king

board = [[0 for x in range(8)] for y in range(8)]

def startCheckers(data, buffer, args): # Start the game
	setupCheckers()
	displayBoard()

	return weechat.WEECHAT_RC_OK

def setupCheckers(): # Sets the default state for every cell of the board
	white = True

	for y in range(8):
		for x in range(8):
			if not white and y <= 2:
				board[x][y] = 1
			elif not white and y >= 5:
				board[x][y] = 2
			else:
				board[x][y] = 0

			white = not white

		white = not white

def displayBoard(): # Displays the board in chat
	message = "\n \nPrinting checkerboard...\n \n. A B C D E F G H\n"
	white = True

	for y in range(8):
		message += str(y) + " "

		for x in range(8):
			state = board[x][y]

			if white:
				message += weechat.color("white,yellow")
			else:
				if state == 1:
					message += weechat.color("black,brown")
				else:
					message += weechat.color("white,brown")

			if state != 0:
				message += (u"\u25CF").encode("utf-8") + " "
			else:
				message += "  "

			white = not white

		message += "\n"
		white = not white

	message += "\n "

	weechat.command("", "/msg " + message)

def checkCheckersInput(data, modifier, modifier_data, string): # Checks every message for checkers input
	weechat.prnt("", str(data))

	return weechat.WEECHAT_RC_OK
