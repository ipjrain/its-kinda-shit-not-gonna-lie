from random import randint
comp = randint(1,100)

while True:
    player = int(input("попробуй угадать число"))
    if comp==player:
        print("вы угадали")
        break
    elif comp != player:
        print("попробуйте еще раз")
        if comp>player:
            print("ваше число меньше")
            player = int(input("попробуй угадать число со второй попытки"))
            if comp==player:
                print("вы угадали")
                break
            elif comp != player:
                player = int(input("попробуй угадать число с третьей попытки"))

                if comp>player:
                    print("ваше число меньше")
                if comp<player:
                    print("ваше число больше")
                if comp==player:
                    print("вы угадали")
                    break
                print("ваше число больше")
            player = int(input("попробуй угадать число со второй попытки"))
            if comp==player:
                print("вы угадали")
                break
                
            elif comp != player:
                ##player = int(input("попробуй угадать число с третьей попытки"))
                if comp<player:
                    print("ваше число больше")
                if comp>player:
                    print("ваше число меньше")
            player = int(input("попробуй угадать число со второй попытки"))
            if comp==player:
                print("вы угадали")
                break
            elif comp != player:
                print("попробуйте еще раз")        
        if comp<player:
            print("ваше число больше")
            player = int(input("попробуй угадать число со второй попытки"))
            if comp==player:
                print("вы угадали")
                break
            if comp>player:
                print("ваше число меньше")
                player = int(input("попробуй угадать число с третьей попытки"))
                if comp>player:
                    print("ваше число меньше")
                if comp<player:
                    print("ваше число больше")
                if comp==player:
                    print("вы угадали")
                    break
  
            if comp<player:
                print("ваше число больше")
                player = int(input("попробуй угадать число с третьей попытки"))
                if comp>player:
                    print("ваше число меньше")
                if comp<player:
                    print("ваше число больше")
                if comp==player:
                    print("вы угадали")
                    break

                     
                            
    else:
        print("мое число было: ",comp)
        
