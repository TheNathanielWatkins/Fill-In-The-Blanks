# This Python file uses the following encoding: utf-8

# IPND Stage 2 Final Project - Nathaniel Watkins

# You've built a Mad-Libs game with some help from Sean.
# Now you'll work on your own game to practice your skills and demonstrate what you've learned.

# For this project, you'll be building a Fill-in-the-Blanks quiz.
# Your quiz will prompt a user with a paragraph containing several blanks.
# The user should then be asked to fill in each blank appropriately to complete the paragraph.
# This can be used as a study tool to help you remember important vocabulary!

# Note: Your game will have to accept user input so, like the Mad Libs generator,
# you won't be able to run it using Sublime's `Build` feature.
# Instead you'll need to run the program in Terminal or IDLE.
# Refer to Work Session 5 if you need a refresher on how to do this.

# To help you get started, we've provided a sample paragraph that you can use when testing your code.
# Your game should consist of 3 or more levels, so you should add your own paragraphs as well!

s = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary, tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

# The answer for ___1___ is 'function'. Can you figure out the others?
# ___2___ arguments
# ___3___ None
# ___4___ list

s_key = (" ", "function", "arguments", "none", "list")

# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd1-1/20min/

import time

log = open("answers.txt", "a")

e = '''Living in the (abbreviation) ___1___ is a privilege in many ways; from the gorgeous scenery to the sense of community, the ___2___ has much to offer its residents. Many individuals who work in the ___3___ ___4___ have also discovered that ___5___ is rapidly being recognized as a ___3___ hub – this is just one more reason to live in Washington State. ___5___ is now home to some of the most successful companies and brands in the ___4___, including Apple, Microsoft, Facebook, and Twitter. If you’re in the ___3___ ___4___ or plan to be after college, you may want to consider the following reasons that ___5___ has risen as a premiere destination for ___3___ ___4___ professionals: \n1: ___5___ is Unique Unto Itself \n2: Working for the Major Players \n3: ___6___ May Have a Better Chance of Survival \n4: ___3___ Conferences'''
# Credit to http://talkingdigital.org/the-rise-of-seattle-as-a-tech-hub/

e_key = ("Easy Answer Key:", "PNW", "region", "tech", "industry", "Seattle", "Startups")

m = '''Seattle, ___1___, is the largest city in the Pacific Northwest. Located between Puget ___2___ and Lake ___1___ in King County, of which it is the county seat, and overlooking Elliott Bay, Seattle is nicknamed The ___3___ City. The city is a damp green gem, with an abundance of evergreen ___4___ throughout, and spectacular views of the Cascade mountains to the ___5___ and the ___6___ mountains to the West. \nThe cultural and business center of the Pacific Northwest, the city and its surrounding areas are the home of the ___7___ Needle, Boeing's aircraft assembly plants, Microsoft, Amazon.com, Costco, Nintendo of America, Starbucks, T-Mobile, and the University of ___1___, as well as a vibrant arts and ___8___ scene and an excellent park system.'''
# Credit to http://wikitravel.org/en/Seattle

m_key = ("Medium Answer Key:", "Washington", "Sound", "Emerald", "trees", "East", "Olympic", "Space", "music")

h = '''Seattle's mild, ___1___ marine climate allows year-round outdoor recreation, including ___2___ing, cycling, hiking, skiing, snowboarding, kayaking, rock climbing, motor-boating, sailing, team sports, and swimming. In town, many people ___2___ around Green Lake, through the forests and along the bluffs and beaches of 535-acre (2.2 km2) ___3___ Park (the largest park in the city) in Magnolia, along the shores of Myrtle ___4___ Park on the Downtown waterfront, along the shoreline of Lake Washington at Seward Park, along ___5___ Beach in West Seattle, or along the ___6___ Gilman Trail. Gas ___7___ Park features the majestic preserved superstructure of a coal gasification plant closed in 1956; located across Lake ___8___ from downtown, the park provides panoramic views of the Seattle skyline. Also popular are hikes and skiing in the nearby ___9___ or Olympic Mountains and kayaking and sailing in the waters of ___10___ Sound, the Strait of Juan de Fuca, and the Strait of Georgia. In 2005, Men's Fitness magazine named Seattle the ___11___ city in the United States.'''
# Credit to https://en.wikipedia.org/wiki/Seattle#Parks_and_recreation

h_key = ("Hard Answer Key:", "temperate", "walk", "Discovery", "Edwards", "Alki", "Burke", "Works", "Union", "Cascade", "Puget", "fittest")

total_guesses = 15 # Sets the max number of incorrect guesses allowed in the whole game.

individual_guesses = 5 # Sets the max number of incorrect guesses allowed for each blank.

# This function handles the beginning of the UI for this game.
def interface():
    toggle = True
    while toggle:
        uInput1 = raw_input("\nWould you like to play a game? > ").lower()
        if uInput1 in ("y", "yes", "yeah", "sure", "affirmative", "yup", "okay", "ok", "yea"):
            print "\nGreat! Let's do a fill-in-the-blanks quiz!"
            while toggle:
                uInput2 = raw_input("\nPlease select a game difficulty by typing it in. > ").lower()
                if uInput2 in ("e", "easy", "simple", "tall", "short" "small", "low"):
                    gameplay("EASY", e)
                    return
                elif uInput2 in ("m", "medium", "middle", "average", "grande", "doubleshot", "mid", "okay", "ok"):
                    gameplay("MEDIUM", m)
                    return
                elif uInput2 in ("h", "hard", "high", "difficult", "venti", "expert", "complex", "tough", "large",):
                    gameplay("HARD", h)
                    return
                elif uInput2 == "sample":
                    gameplay("SAMPLE", s)
                    return
                else:
                    print 'Your response was not recognized as "easy", "medium", or "hard" please try again.'
        elif uInput1 in ("n", "no", "nah", "nope", "negative", "nix"):
            print "\nOkay. Your loss..."
            toggle = False
            return
        elif uInput1 == "Oh!":
            print "\nhttp://www.imdb.com/title/tt0086567/quotes\nGood job on getting the reference, but let's try again for a yes or no answer."
        else:
            print '\nYour response was not recognized as a "Yes" or "No", please try again.'

# This function handles the core gameplay elements of cycling through the paragraph looking for blanks and announcing when they win.
def gameplay(difficulty, selectedParagraph):
    print "You've selected {0} mode!\n\nYou will get {1} guesses per question, or {2} incorrect guesses total, whichever comes first.\n\nHere is the {0} difficulty paragraph.  Please fill in all the numbered blanks by answering the following questions.\n".format(difficulty, individual_guesses, total_guesses)
    replaced = []
    replaced = selectedParagraph.split()
    num = 1
    while "___{0}___".format(num) in replaced:
        print " ".join(replaced)
        fillIn(replaced, num, difficulty, individual_guesses)
        num += 1
    print "\nCongratulations!  You win!!!\n\nHere's the correct statement:\n"
    print " ".join(replaced) + "\n"

# This function handles what happens when they guess correctly or incorrectly.
def fillIn(replaced, num, difficulty, individual_guesses):
    index = -1
    global total_guesses
    for word in replaced:
        index += 1
        blank = "___{0}___".format(num)
        if blank in word:
            guesses = 0
            guess = guessing(num, difficulty)
            while guess is False:
                guesses += 1
                total_guesses -= 1
                if (guesses == individual_guesses) or (total_guesses == 0):
                    raise SystemExit("\nGame Over! You have failed too many guesses.")
                elif (guesses == (individual_guesses - 1)) or (total_guesses == 1):
                    print "\nThat still isn't the correct answer. Warning! This is your last try.  Make it count!"
                else:
                    print "\nThat isn't the correct answer. You have {0} trys left and {1} total trys left.".format((individual_guesses - guesses), (total_guesses))
                guess = guessing(num, difficulty)
            if guess:
                answer = setAnswer(num, difficulty)
                if blank == word:
                    replaced[index] = answer
                    print "\nCorrect!\n"
                    fillAll(replaced, num, difficulty)
                else:
                    replaced[index] = word[:word.index(blank)] + answer + word[word.index(blank) + len(blank):]
                    print "\nCorrect!\n"
                    fillAll(replaced, num, difficulty)

# This function handles checking whether the answer is True, or False.  False answers get logged in answers.txt
def guessing(num, difficulty):
    attempt = (raw_input("\nWhat should be substituted for ___{0}___? > ".format(num))).lower()
    if attempt == setAnswer(num, difficulty).lower():
        return True
    else:
        log.write(time.strftime("%c") + " | {0}{1} | incorrect answer: ".format(difficulty[0], num) + attempt + "\n")
        return False

# This function handles filling in all the remaining blanks of the same word once they've guessed the first instance correctly.
def fillAll(replaced, num, difficulty):
    index = -1
    for word in replaced:
        index += 1
        blank = "___{0}___".format(num)
        if blank in word:
            answer = setAnswer(num, difficulty)
            if blank == word:
                replaced[index] = answer
            else:
                replaced[index] = word[:word.index(blank)] + answer + word[word.index(blank) + len(blank):]

# This function sets the reference list of answers to pull from.
def setAnswer(num, difficulty):
    if difficulty == "EASY":
        answer = e_key[num]
        return answer
    elif difficulty == "MEDIUM":
        answer = m_key[num]
        return answer
    elif difficulty == "HARD":
        answer = h_key[num]
        return answer
    elif difficulty == "SAMPLE":
        answer = s_key[num]
        return answer
    else:
        print "Unexpected Result"
        log.write(time.strftime("%c") + " | UR | setAnswer: " + difficulty + " " + num + "\n")

interface()
