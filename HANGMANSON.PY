word = "mmmeeeetaall" ## buradan kelimeyi değiştirebiliriz - you can change the word here.

word_list = list(word)   ## kelimenin içinde herhangi bir harf dörtden den fazla varsa çalışmaz.
                         ## the programme cannot run the word that have four and more same letters
name = input("Hello, enter your name to begin :") ## Melih Çeliktaş

hp = 10

print (f"{name} time to play hangman!")

print (f"You have {hp} hp")


hm_list = []


x = len(word)
i = 0

while i < x:

    hm_list.append("-")

    i += 1




for element in hm_list:
    print(element)



while hp > 0:


    if "-" not in hm_list:

            hp == -1

            print("you won!")

            break


    letter = input("enter a letter:")

    if letter in word_list:

        if word_list.count(letter) == 1:

            hm_list[word_list.index(letter)] = letter.upper()

            for element in hm_list:
                print(element)

        elif word_list.count(letter) == 2:

            hm_list[word_list.index(letter)] = letter.upper()

            hm_list[word_list.index(letter, word_list.index(letter)+1, x)] = letter.upper()

            for element in hm_list:
                print(element)

        elif word_list.count(letter) == 3:

            hm_list[word_list.index(letter)] = letter.upper()

            hm_list[word_list.index(letter, word_list.index(letter)+1, x)] = letter.upper()

            a = word_list.index(letter, word_list.index(letter)+1, x)

            hm_list[word_list.index(letter, a+1, x)] = letter.upper()

            for element in hm_list:
                print(element)

        elif word_list.count(letter) == 4:


            hm_list[word_list.index(letter)] = letter.upper()

            hm_list[word_list.index(letter, word_list.index(letter)+1, x)] = letter.upper()

            a = word_list.index(letter, word_list.index(letter)+1, x)

            hm_list[word_list.index(letter, a+1, x)] = letter.upper()

            b = word_list.index(letter, a+1, x)

            hm_list[word_list.index(letter, b+1, x)] = letter.upper()

            for element in hm_list:
                print(element)






    else:
        hp = hp - 1

        print ("Wrong!")

        print (f"You have {hp} hp")

if hp == 0:
    print ("You lost!")


