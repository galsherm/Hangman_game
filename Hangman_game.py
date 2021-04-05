import time
def opening():
    """
    This function save the name of the game to string in ASCII_ART.
        :parm : nothing
        :type secret_word:void
        :return: string of all the name of the game
        :rtype:string
     """
    HANGMAN_ASCII_ART  = """
      _    _                                         
     | |  | |                                        
     | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
     |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
     | |  | | (_| | | | | (_| | | | | | | (_| | | | |
     |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                          __/ |                      
                         |___/
                            
     """ 
    return HANGMAN_ASCII_ART   

        
def choose_word(file_path, index): 
    """
    This function choose word from location in the compuer.
        :parm file_path: The file path of the text file that all the secret_word are save
        :parm index: the index of the word in file9start with 1)
        :type file_path:string
        :type index: integer
        :return: secret word that the user need to guess
        :rtype:string
    """
 
    my_dict = {}
    my_list = []
    found  = 0
    cnt = 0
    choosen_word = ""
    input_file = open(file_path,"r")  
    for line in input_file:
       for word in line.split():
           my_list.append(word)
           cnt += 1
           if cnt == index and found ==0:
               found = 1
               choosen_word = word
           my_dict[word] = "*"
    if found == 0:
       cnt = index -1
       for elem in my_list:
           cnt += 1
           if cnt == index:
               choosen_word = elem               
    return (len(my_dict),choosen_word)
     
def check_valid_input(letter_guessed, old_letters_guessed =[]):
    """
    This function check if the letter guessed by the player is correct.
        :parm letter_guessed: letter guessed by the player
        :parm old_letters_guessed: list of old_letters_guessed by player
        :type letter_guessed:string
        :type old_letters_guessed: list
        :return: True if the letter is from english letter and if it just one letter and not include in old_letters_guessed list  else return False
        :rtype:bool
     """
##tav lo takin ##  
    letter_guessed_tikon = letter_guessed.lower()
    if (len(letter_guessed_tikon) > 1) or (letter_guessed_tikon.isalpha() == False) or  (letter_guessed_tikon in old_letters_guessed ):
        return False
##             ##   


##correct char    ##
    if (len(letter_guessed_tikon) == 1) and (letter_guessed_tikon.isalpha() == True) and (letter_guessed_tikon not in old_letters_guessed) :
        old_letters_guessed.append(letter_guessed_tikon) 
        return  True   
        
def try_update_letter_guessed(letter_guessed, old_letters_guessed ): 
    """
        This function check if the letter guessed by the player is correct
        :parm letter_guessed: letter guessed by the player
        :parm old_letters_guessed: list of old_letters_guessed by player
        :type letter_guessed:string
        :type old_letters_guessed: list
        :return: True if the letter is from english letter and if it just one letter and not include in old_letters_guessed list  else  print list of all the letters in old_letters_guessed by the player (except the current letter) and returnFalse
        :rtype:bool
     """
##incorrect char ##
      
    letter_guessed_tikon = letter_guessed.lower()

    if (len(letter_guessed_tikon) > 1) or (letter_guessed_tikon.isalpha() == False) or  (letter_guessed_tikon in old_letters_guessed ):
        print("X")
        old_letters_guessed.sort() 
        seperator = ' -> '
        print("All the letters you have guessed so far:  ",seperator.join(old_letters_guessed))
        return False
        
##             ## 

##correct char ##
    if (len(letter_guessed_tikon) == 1) and (letter_guessed_tikon.isalpha() == True) and (letter_guessed_tikon not in old_letters_guessed) :
        old_letters_guessed.append(letter_guessed_tikon) 
        return  True
        
def show_hidden_word(secret_word, old_letters_guessed): 
    """
    This function put letters in correct place of the secret word.
        :parm secret_word: this is the secret word that the user cannot seek
        :parm old_letters_guessed: the letters gueess by the user
        :type secret_word:string
        :type old_letters_guessed: list
        :return: string of all the correct letters that eas guess by the user
        :rtype:string
     """
    
    cnt = -1
    my_list = []
    for i in secret_word:
        my_list.append("_")    
    for user_char in old_letters_guessed :
        cnt = -1
    
        for elem in secret_word :
            cnt += 1
            if elem == user_char:
               my_list[cnt] = user_char 
   
        present_str =' '.join(my_list)
    return present_str
    
def check_win(secret_word, old_letters_guessed): 
    """This function check if the user guess all the letters in the secret_word
        :parm secret_word: this is the secret word that the user cannot seek
        :parm old_letters_guessed: the letters gueess by the user
        :type secret_word:string
        :type old_letters_guessed: list
        :return: "True" if user gueess was right else return "False"
        :rtype:bool
    """
    cnt = -1
    my_list = []
    for i in secret_word:
        my_list.append("_")  
    for user_char in old_letters_guessed :
        cnt = -1    
        for elem in secret_word :
            cnt += 1
            if elem == user_char: 
               my_list[cnt] = user_char 
    if ''.join(my_list) ==  secret_word:
        return True
    else:
        return False
def print_hangman(num_of_tries):
    HANGMAN_PHOTOS = {
    1 : "\npicture 1: x-------x",
    2 : 
    """
    picture 2:
        x-------x
        |
        |
        |
        |
        |
        |
     """,
     3 : 
    """
    picture 3:
        x-------x
        |       |
        |       0
        |
        |
        |    
    """,
     4 :
     """
    picture 4:
        x-------x
        |       |
        |       0
        |       |
        |
        |   
    """,
     5 :
     """
    picture 5:
        x-------x
        |       |
        |       0
        |      /|\\
        |
        | 
     """,
     6 :
     """
    picture 6:
        x-------x
        |       |
        |       0
        |      /|\\
        |      /
        | 
     """,
     7 :
     """
     picture 7:
    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |
    """
     
        }
    if num_of_tries == 1:
       print(HANGMAN_PHOTOS.get(1)) 
    elif num_of_tries == 2:
       print(HANGMAN_PHOTOS.get(2))
    elif num_of_tries == 3:
       print(HANGMAN_PHOTOS.get(3)) 
    elif num_of_tries == 4:
       print(HANGMAN_PHOTOS.get(4))
    elif num_of_tries == 5:
       print(HANGMAN_PHOTOS.get(5)) 
    elif num_of_tries == 6:
       print(HANGMAN_PHOTOS.get(6))
    elif num_of_tries == 7:
       print(HANGMAN_PHOTOS.get(7)) 
               
import random     
def main():
   MAX_TRIES = 6
   old_letters_guessed = []  
   cnt = 1
   word = ""

   print(opening()) 
   
    
   my_tuple = choose_word(r"E:\text_files\words.txt",1)
   num_of_words_in_file = int(my_tuple[0])
   my_tuple = choose_word(r"E:\text_files\words.txt", random.randint(1,  num_of_words_in_file) ) 
   game_board_word = my_tuple[1]
   print("\n\n")

   print( "_ "*len(game_board_word))  
   print("\n")
   letter_guessed=input("Guess a letter: ") #first letter
   if  check_valid_input(letter_guessed.lower() , old_letters_guessed) == False :# tav lo takin
       print(letter_guessed.lower())
       print_hangman(1) 
       old_letters_guessed.append(letter_guessed)
       word = show_hidden_word(game_board_word, old_letters_guessed)      
      
       print("Please enter valid english letter\n")
   else:                                                                #tav takin
       print(letter_guessed.lower())
       word = show_hidden_word(game_board_word, old_letters_guessed)   
       
       if letter_guessed not in game_board_word:  #if letter guessed wrong not in secret word
           print_hangman(cnt)
       elif letter_guessed  in game_board_word:
            print(word)
       if  check_win(game_board_word, old_letters_guessed) == True:
           print("You win")
           print("valid letters you have guess : ",show_hidden_word(game_board_word, old_letters_guessed)) 
           return   

        
   while  MAX_TRIES != 0:
        MAX_TRIES -= 1
        cnt +=1
        
        letter_guessed=input("Guess a letter: ") # second letter
        print(letter_guessed.lower())
   
        if  try_update_letter_guessed(letter_guessed, old_letters_guessed ) == False : # tav not takin 
            print_hangman(cnt)
            if MAX_TRIES >1:
                print("\nPlease enter valid english letter that you not guessed yet\n")
        else:                                                                          #tav takin
            #if player guess tav takin but it is not equal to the game_board_word 
            if word == show_hidden_word(game_board_word, old_letters_guessed):
                print_hangman(cnt)
                word = show_hidden_word(game_board_word, old_letters_guessed)

            else:                                                                    #player guessed tav taakin from the secret word
                if  check_win(game_board_word, old_letters_guessed) == True:
                    print("valid letters you have guess : ",show_hidden_word(game_board_word, old_letters_guessed)) 
                    print("You win")
                    time.sleep(5)
                    return
                word = show_hidden_word(game_board_word, old_letters_guessed)
                MAX_TRIES += 1  #if player right so he have got more chances
                cnt -= 1        #fit the right images num
                print(word)
   if  check_win(game_board_word, old_letters_guessed) == False:             
       print("You loose\nThe word was:\n")  
       print(game_board_word)
       time.sleep(5)

      
if __name__ == "__main__":
    main()  