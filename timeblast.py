iimport sys, select, os, time
from random import randint
from termios import tcflush, TCIOFLUSH
limit = 600
random_number = randint(0,9)
success = False
print("What level are you at?")
print("1. Beginner")
print("2. Intermediate")
print("3. Motherfucker")
level = int(input(""))

if(level == 1):
    timer = 30
    chances = 5
elif(level == 2):
    timer = 20
    chances = 3
else:
    timer = 10
    chances = 1
while(chances and not success):
    for i in range(limit, 1, -1):
        os.system('cls' if os.name == 'nt' else 'clear')

        print("Your lucky number is  " + '\x1b[9;30;45m' + "      " + str(random_number) + "      " + '\x1b[0m')

        print("Press ENTER      =>   " + '\x1b[1;30;47m' + "     " + str(i) + "    " + '\x1b[0m')
        if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
            tcflush(sys.stdin, TCIOFLUSH)
            break
        i += 1
        time.sleep(timer/100)

    chances = chances - 1
    if i%10 == random_number:
        print('\x1b[2;35;47m' + "You are the hero they need but don't deserve" + '\x1b[0m')
        success = True
    else:
        print('\x1b[1;32;41m'+ "***BOOOOOOOOOOMMMM***" + '\x1b[0m')
        if(chances):
            print("Chances Remaining are " + '\x1b[1;37;40m' + "      " + str(chances - 1) + "      " + '\x1b[0m')
            print("Game would restart in 3 seconds")
            time.sleep(3)
        # for i in range(3,1,-1):

