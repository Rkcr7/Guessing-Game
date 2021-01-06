import eel
import random
num = random.randint(1,100)
eel.init("web")
@eel.expose
def intro():
    print("WELCOME TO GUESS ME!")
    print("I'm thinking of a number between 1 and 100")
    print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
    print("If your guess is within 10 of my number, I'll tell you you're WARM")
    print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
    print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
    print("LET'S PLAY!")


guesses = [0]
print(num)




@eel.expose
def value(numb):
    
    
    guess=int(numb)

    if guess < 1 or guess > 100 or str(guess)=='':


        return('OUT OF BOUNDS: ')
    
        
    
    # here we compare the player's guess to our number
    if guess == num:
        
        return (f':YEAH, YOU GUESSED IT IN ONLY {len(guesses)} GUESSES!')

        
        
        
    # if guess is incorrect, add guess to the list
    guesses.append(guess)
    
    # when testing the first guess, guesses[-2]==0, which evaluates to False
    # and brings us down to the second section
    
    if guesses[-2]:  
        if abs(num-guess) < abs(num-guesses[-2]):
            print('WARMER!')
            return ":WARMER"
            
        else:
            print('COLDER!')
            return ":COLDER"
            
   
    else:
        if abs(num-guess) <= 10:
            print("warm")
            return ":WARM!"
            
        else:
            print("COLD")
            return ':COLD!'
            

    
    
    

        # we can copy the code from above to take an input
        
@eel.expose
def guest():
    a=(len(guesses)-1)
    print(a)
    return("-----:" + str(a))
eel.start('index.html',port=8000)  # Starting the App