import random, os, time

die     = ["   \n O \n   "]   #1
die.append("  O\n   \nO  ")   #2
die.append("O  \n O \n  O")   #3
die.append("O O\n   \nO O")   #4
die.append("O O\n O \nO O")   #5
die.append("O O\nO O\nO O")   #6

def animate_die():
  for roll in range(0,6):
    os.system('clear')
    print("\n")
    number = random.randint(0,5)
    print(die[number])
    time.sleep(2)
  
#Main Program Starts Here....


fortunes=["you'll never get your drivers licens or you'll lose them",
"You'll some how get 20 bucks today.",
"you'll get money from Mr.Krabbs.",
"Squidward took all of your money.",
"I don't think you paid me enough",
"here's a refund You've recieved 3050 bucks",
"You gotta pay extra",
"you will find true love",
"your ture love is in study hall",
"you will have a good day",
"you will get a good grade on your test",
"you will be rich",
"you will make someone smile today",
"you will be happy today", 
"hmmmm",
"you will find true love,but not today",
"you will die",
"you made $10,000",
"you will pay $100",
"you will cook a egg",
"your car breaks",
"you will make a band",
"you get hit by a car",
"you will not find true love ever",
"you will have a bad day",
"i dont feel like telling you, go away",
"you might find love, maybe",
"figure it out yourself",
"your soulmate hates you and will never love you!",
"AI will takeover the world",
"You do not have a fortune. try again",
"overweight",
"homeless",
"smell like garbage can",
"your mom cheats on your dad and they get divorced",
"win $1,000,000",
"dog run over by mailman",
"crash car into tree",
"drug dealer",
"Your other sister died",
"Your sister died",
"Your brother died",
"Your aunt died",
"Your dad died",
"Your mom died",
"Your uncle died",
"you died",
"Your study hall closed your chat with your valentine",
"You got blocked",
"Your crush likes you back",
"Ghosted",
"She's your valentine",
"She's not yours",
"She already has a valentine",
"You got friendzoned",
"u got blocked ",
" u finna be alone",
" she busy jitt",
" unc got her",
" try again in a couple months",
" he going to answer the ft",
"she gon  have to pass on alldat",
"ion",
"You will pass all of your classes",
"You will get a dog",
"You will die soon",
"You will get a cat",
"You will become Batman",
"You will become Robin",
"You will become Alfred",
"You will get $1,000,000",
"Your study hall monitor just closed your chat with your valentine",
"You got blocked.",
"You'll be good at baseball",
"You'll pass school perfectly",
"Your valentine will ask you out",
"You will be rich",
"You will be able to hangout with your friends",
"Your life will be as you choose",
"Hope you had fun",
"You will find true, love but not today",
"Your true love is in study hall but you cant't talk to them",
"Hmmmm. IDK. Kind of hazy. Try again",
"You will find true love, but not today",
"Look up.",
"You will have a very lovely day today",
"Happiness through buddhism",
"You now have a 5% higher chance of being struck by a lightning bolt",
"Death",
"You will float randomly at the most important time of your life",
"Your next pizza order will mistakenly have anchovies on it",
"Hmmm. I don't know. Try again",
"Good fortune is yours!",
"Someone is thinking of you.",
"Welcome change.",
"You will have good luck today!",
"Good news will come to you by text.",
"New ideas could be profitable.",
"Others can help you now.",
"Soon life will become more interesting.",
"you will find true love, but not today",
"you our love is in studay hall",
"mcdonalds is your true love",
"vucovik is the coolest friend you have"
"vucovik is still your best friend",
"FORTNITE BATTLE PASS AMONG US OHIO MR BEAST EDITION V6",
"Llama",
"stop playing these childish games",
"A new opportunity will reveal itself to you.",
"Something good will come of today.",
"Something bad is approaching.",
"Someone has something to say to you.",
"One of your dreams is in reach.",
"Your future is looking bright.",
"I'm hungry.",
"Show your appreciation for others more.",
"unadded",
"you smell awful",
"you got broken up wit",
"she busy lil bro",
"cheated on",
"haircut by fisher ):",
"ugly",
"Your study hall monitor just closed your chat with your valentine",
"You got blocked.",
"No thank you.",
"I has boyfriend.",
"No response.",
"Mom said no.",
"I'm busy that day.",
"Sure!",
"You will die",
"you'll get a brand new house",
"you have to spend a day with x",
"you can skip programming 2 for a week!",
"You'll never get a girlfriend",
"your taxes will go up again",
"You'll get a bad haircut",
"that wasn't one of the numbers...",
"your study hall monitor just closed your chat with your valentine",
"you got blocked.",
"no thank you",
"i have a boyfriend",
"no cookies",
"monkey",
"you are short",
"sure!",
"your study hall monitor just closed your chat with your valentine",
"you got blocked.",
"Your valentinte thought you were someone else",
"your valentine forgot who you were",
"You'll have a bad hair day",
"Something great might happen to someone dear to you",
"You'll soon face your fear",
"You'll meet an unsuspected old forgoten friend",
"Your truck will never be done",
"Your truck will be done",
"Your truck will be half way done",
"You bought a new truck instead",
"You sold it... dissapointed",
"You bought a used one...",
"You gave up...dang",
"Your truck will be qauter way done",
"you will become famous",
"you will be jumped on your way home from school",
"your dad will leave you very soon",
"You will move into a mansion with a buttler and maid",
"you will meet and marry you celebrity crush",
"you will get arrested over the weekend",
"You will find laughter and joy in something very unexpected",
"Your mom will win the jackpot but won't give you any of it",
"you won't get a srt",
"you won't get a cookie",
"your grandma will fall down the stairs",
"you will stub your toe",
"you won't get candy",
"you will die",
"you will loose a finger",
"you won't make it into the fncs",
"you will never win a nitro type game again",
"Play fortnite all day",
"Get the fortnite battle pass",
"Drink the grimace shake",
"Burn your house down",
"Break all of Dalton's skateboards",
"Try again bruh",
"You will hit the griddy during superbowl 83 and collapse from a heart attack due to eating 78 white castle sliders",
"You will find love within this lifetime. You are also immortal ",
"You will find a penny laying face-up on a staircase in 36 days and 2 hours ",
"You will meet the person responsible for putting the alphabet in math through time travel and have an epic war spanning 40 years, 50 million soldiers and all 7 continents ",
"Your day will be better than usual ",
"Basically, you'll die ",
"You will lead the last cavalry charge in the Holy Millenium War against the immortal dying a martyr to the cause of ending the 50 generation galactic war ",
"Your next lasagna will be above average ",
"Your daddy finally came home",
"Your daddy finally left you",
"You will crash your car",
"You will meet your future partner",
"You gonna fail that test",
"Your bestie is eating your lunch",
"I see nothing in you",
"OOPS, your device crashed.",
"You will be rich one day",
"You will nit win the lottery",
"You will hit Champion rank in Rainbow Six Siege",
"You will win the lottery",
"You will be a great leader",
"You will be Copper Rank for the whole season in Rainbow Six Siege",
"You will be the greatest streamer ever",
"You will get $20"]
print("I am the amazing fortune teller Mr. Vukovic!!!\n\n")
print("""
,(  #/(%(#%#%###(((((# .,%#&%%(*   %#%%#&%&&&%%&@&@@&&&&&%&%%&&/#(*,(,%% %%/%#/(
(#%%##%(//%#%*//*.%&%,(##((&&&%(#####%(*,*&/#@@%&&@&&&&&#%#%@&&##((., /(*#(*%,*/
#%####%&%%#%%/%%%&%#%#((/**/#%&(%%#(#(%#/((/#((/(#&@@#&##@%&&&#*,/#/#*,(##%/,,*/
(%*%%#%%&%(/&%%(#%%*(   /%#%%*&/(%#/((#((//(%##%#(#&&&%&#&%%%%&# /%&#(**/**.#/*.
(%%%#%%#%(*/(#%%#((//*/####(*//*////(//((((((((##(%(/&#&&%(&%%&##, #.// ((*(*/*,
%#%//(##((&%#%%#%(#((%%/*,,,,,,,,....,,,******/*,  /#,%&@#%%%&%(%###(,. ( *(##**
#%//(%%%%#%#%%%%%%#/((*,,,,,...,,,,,,*,***///(((//,,,/*#&%#%@&%%%%/(*#(#*##*,((#
(&&&&#@%#%&%%%%((%%************/******//////(((((/(//**,%#%%@&%*%%%((#/%#(#((%(%
##(%&#%%@@&##%#&#((/****,,,*,,.,,,,****/,****///////(((*/%#&@&(((, #%*%/(#*##((,
@%#&&&&%#@%#%%#%#((/*/****,,,,,,,********//(((##(((/((((/&&@%%(((/(*#,/(%*%#((,.
%##%#&%&@&%%&&@@&%&///*****///(((((((((((#%%%%%%#(%##(((#@@%&@#((#(*%#((**%,(.(*
*#&#%&&&%&&%&@&@%@@////(##%%&&&%%%%##%%%&&&@&@@&&&&&&%#((#%&%&#(#/((*//(*#(#***#
&@@@@@&&%#%@@@@@@@&#//((/*//(%%&&&%#*,*#&@@@@@@@@@@&%%#((#%%@&(##/,/,(//((/*/.#(
@@@@@@@@&%##&@@@&@@(/*/#&##%#(%%%#(/*,*(&%&&%%%%%&&&#((((&@&%&((**/**,  ,.   ,*/
@@@@@@&@@@&&@&&%@@&&(*,,,,*(((*******,*(#%%#(/******///((%@@&%  .       ...     
@@@@@&%&@&@@@@#%@@%#(/**,,,,,***,****,,/(%%%(/***/////(#((/&&@*..              .
@@@@@@@@&&&&%&&@&&%#,/******/////#***,,/(///%#(/(((###%%#&/#@@           ...*,%/
&@@&&@@&&%@%&(#%@@@@,//////((((#//////(#%&&&&%%##%%%&&&%#@&@@&.              **,
@@@@@&%@&@#####@%&&%@%((((((##(////#%&@&&@@@&&%&&@&&&&&%#&%&&%&  ,.,,,., .  ,.,.
%%%&@&&&@@#%/.@@###%%%((((((((%#((((##&&&&@&&&@@&%#%&&&%###%&&&%,,...,,,,,,.****
#%%%##%%%&&@@@%@@&@@@@((((//(%%/*////(&@&&&&%%#%%%#%&&%##&%%&&&&&&%****///*/*//*
&@@#(&@%%%@@@@@(@&%&@@@, ((((((((((((#%%&&&&&&&&%%&&&%.  #@&&&%&&@&#/**/*/////**
@@@@@@@@*&&%%@@&&&&#     ./(((((////***//((##(##%&&&(**.*,...    *%%%(###(((((/(
&@@@&&##%#%#%#        ,  ..,,(#(//****/(//((#(#%&%&(/**,,,,,*....    .(##(#(((((
@@%%%#&###            .,  .,.*//(((((#%&##%%&&%&&&#((/*****,.,...,..., .((#(#(((
&@&%###   .  .  .   .  ,   ,  /(((##%%%%%%&&&@@%##(*//****,,,,,...,,,,.,.*##((##
@%#      ......  , ..,.,,,,((((,*((#####%%&@&@@@&(*////(*/,,,,*,..,.,.,.*,,,(((""")



play=input("Hello, would you like me to tell your fortune?  ").lower()
if(play !='yes'):
    print("Goodbye!!!")
else:
    while(play=="yes"):
        color=input("Please choose a color: red, blue, orange, or green:  ").lower()
        length=len(color)
        #print(length)
        if(length % 2==0):#even
            number1=input("Please choose a number: 1, 2, 5, or 6:  ")  
            number1=int(number1)
            if(number1 % 2==0):
                number2=int(input("Please choose a number: 1, 2, 5, or 6:  "))
            else:
                 number2=int(input("Please choose a number: 3, 4, 7, or 8:  "))   

        else: #odd
            number1=input("Please choose a number: 3, 4, 7, or 8:  ")    
            number1=int(number1)
            if(number1 % 2==1):
                number2=int(input("Please choose a number: 1, 2, 5, or 6:  "))
            else:
                 number2=int(input("Please choose a number: 3, 4, 7, or 8:  "))
        fortune=random.choice(fortunes)
        animate_die()
        print("\n\nYour fortune:  "+fortune)
        play=input("\n\nWould you like me to tell you another fortune? yes/no:  ").lower()
        
print("Goodbye!!!")
