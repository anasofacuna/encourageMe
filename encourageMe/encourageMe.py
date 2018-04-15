import random

def main():
	encFile = open('encouragements.txt','r')
	encouragement = encFile.readlines()
	helpMe = ""
	while(helpMe != "stop"):
		encIn = random.randint(0,len(encouragement) - 1)
		print(encouragement[encIn])
		helpMe = input("Do you still need encouragement? Feel free to tell me to stop ")

	print("I hope you feel encouraged!!! <3")
	more = input(("If you have any other words of encouragement, please input one here! Otherwise, goodbye!"))
	encOut = open('encouragements.txt', 'a')
	if (more != "goodbye"):
		encOut.write("\n" + more)


main()