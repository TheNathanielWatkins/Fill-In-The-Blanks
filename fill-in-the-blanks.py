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

answers = open("answers.txt", "a")

e = '''Seattle, ___1___, is the largest city in the Pacific Northwest. Located between Puget ___2___ and Lake ___1___ in King County, of which it is the county seat, and overlooking Elliott Bay, Seattle is nicknamed The ___3___ City. The city is a damp green gem, with an abundance of evergreen ___4___ throughout, and spectacular views of the Cascade mountains to the ___5___ and the Olympic mountains to the ___6___ . The cultural and business center of the Pacific Northwest, the city and its surrounding areas are the home of the ___7___ Needle, Boeing's aircraft assembly plants, Microsoft, Amazon.com, Costco, Nintendo of America, Starbucks, T-Mobile, and the University of ___1___, as well as a vibrant arts and ___8___ scene and an excellent park system.'''
# Credit to http://wikitravel.org/en/Seattle

e_key = ("", "Washington", "Sound", "Emerald", "trees", "East", "West", "Space", "music")

m = '''Living in the ___1___ is a privilege in many ways; from the gorgeous scenery to the sense of community, the region has much to offer its ___2___ . Many individuals who work in the ___3___ ___4___ have also discovered that ___5___ is rapidly being recognized as a ___3___ hub – this is just one more reason to live in Washington State. ___5___ is now home to some of the most successful companies and brands in the ___4___, including Apple, Microsoft, Facebook, and Twitter. If you’re in the ___3___ ___4___ or plan to be after college, you may want to consider the following reasons that ___5___ has risen as a premiere destination for ___3___ ___4___ professionals: \n*___5___ is Unique Unto Itself \n*Working for the Major Players \n* ___6___ May Have a Better Chance of Survival \n*___3___ Conferences'''
# Credit to http://talkingdigital.org/the-rise-of-seattle-as-a-tech-hub/

m_key = ("", "PNW", "residents", "tech", "industry", "Seattle", "Startups")

h = '''Seattle's mild, ___1___ , marine climate allows year-round outdoor recreation, including ___2___ing, cycling, hiking, skiing, snowboarding, kayaking, rock climbing, motor-boating, sailing, team sports, and swimming. \nIn town, many people ___2___ around Green Lake, through the forests and along the bluffs and beaches of 535-acre (2.2 km2) ___3___ Park (the largest park in the city) in Magnolia, along the shores of Myrtle ___4___ Park on the Downtown waterfront, along the shoreline of Lake Washington at Seward Park, along ___5___ Beach in West Seattle, or along the Burke-Gilman ___6___ . Gas ___7___ Park features the majestic preserved superstructure of a coal gasification plant closed in 1956. Located across Lake ___8___ from downtown, the park provides panoramic views of the Seattle skyline. \nAlso popular are hikes and skiing in the nearby Cascade or ___9___ Mountains and kayaking and sailing in the waters of ___10___ Sound, the Strait of Juan de Fuca, and the Strait of Georgia. In 2005, Men's Fitness magazine named Seattle the ___11___ city in the United States.'''
# Credit to https://en.wikipedia.org/wiki/Seattle#Parks_and_recreation

h_key = ("", "temperate", "walk", "Discovery", "Edwards", "Alki", "Trail", "Works", "Union", "Olympic", "Puget", "fittest")

diff_string = 0

total_guesses = 15

# This function handles the beginning of the UI for this game.
def interface():
    global diff_string
    toggle = True
    while toggle:
        answer1 = raw_input("\nWould you like to play a game? > ").lower()
        if answer1 in ("y", "yes", "yeah", "sure", "affirmative", "yup", "okay", "ok", "yea"):
            print "\nGreat! Let's do a fill-in-the-blanks quiz!"
            while toggle:
                answer2 = raw_input("\nPlease select a game difficulty by typing it in. > ").lower()
                if answer2 in ("e", "easy", "simple", "tall", "short" "small", "low"):
                    diff_string = e
                    instructions("easy")
                    return
                elif answer2 in ("m", "medium", "middle", "average", "grande", "doubleshot", "mid", "okay", "ok"):
                    diff_string = m
                    instructions("medium")
                    return
                elif answer2 in ("h", "hard", "high", "difficult", "venti", "expert", "complex", "tough", "large",):
                    diff_string = h
                    instructions("hard")
                    return
                elif answer2 == "sample":
                    diff_string = s
                    instructions("sample")
                    return
                else:
                    print 'Your response was not recognized as "easy", "medium", or "hard" please try again.'
        elif answer1 in ("n", "no", "nah", "nope", "negative", "nix"):
            print "\nOkay. Your loss..."
            toggle = False
            return
        elif answer1 == "Oh!":
            print "\nhttp://www.imdb.com/title/tt0086567/quotes\nGood job on getting the reference, but let's try again for a yes or no answer."
        else:
            print '\nYour response was not recognized as a "Yes" or "No", please try again.'

# This function handles the UI for giving the player the basic instructions.
def instructions(difficulty):
    print "You've selected {0} mode!".format(difficulty.upper())
    print "\nYou will get 5 guesses per question, or {0} incorrect guesses total, whichever comes first.".format(total_guesses)
    if difficulty in ("easy", "medium", "sample"):
        print 'And if you would like to pass on a blank to fill it in later, you can just type "PASS" (note the all-caps) to come back to that question after the others.'
        gameplay(difficulty, True)
    elif difficulty == "hard":
        gameplay(difficulty, False)
    else:
        print "Unexpected Result"
        answers.write(time.strftime("%c") + " | UR | instructions:" + difficulty + "\n")

# This function handles the core gameplay elements of cycling through the paragraph looking for blanks and announcing when they win.
def gameplay(difficulty, next):
    print "\nHere is the {0} difficulty paragraph.  Please fill in all the numbered blanks by answering the following questions.\n".format(difficulty.upper())
    global e, m, h, s, diff_string, answers
    replaced = []
    replaced = diff_string.split()
    # answers.write(time.strftime("%c") + " | TR | " + difficulty + ": " + str(replaced) + "\n")
    num = 1
    while "___{0}___".format(num) in replaced:
        print " ".join(replaced)
        pass_check = fillIn(replaced, num, difficulty)
        if pass_check == "PASS" and next is True:
            pass # TODO
        num += 1
    print "\nCongratulations!  You win!!!\n\n Here's the correct statement:\n"
    print " ".join(replaced)

# This function handles what happens when they guess correctly or incorrectly.
def fillIn(replaced, num, difficulty):
    index = -1
    global total_guesses
    for word in replaced:
        index += 1
        blank = "___{0}___".format(num)
        if blank in word:
            guesses = 0
            guess = guessing(num,difficulty)
            while guess is False:
                guesses += 1
                total_guesses -= 1
                if (guesses == 5) or (total_guesses == 0):
                    raise SystemExit("\nGame Over! You have failed too many guesses.")
                elif (guesses == 4) or (total_guesses == 1):
                    print "\nThat still isn't the correct answer. Warning! This is your last try.  Make it count!"
                else:
                    print "\nThat isn't the correct answer. You have {0} trys left and {1} total trys left.".format((5 - guesses), (total_guesses))
                guess = guessing(num,difficulty)
            # except ValueError:
            #     print "Unexpected Result"
            #     answers.write(time.strftime("%c") + " | UR | fillIn: " + blank + "\n")
            if guess:
                answer = setAnswer(difficulty, num)
                if blank == word:
                    replaced[index] = answer
                    print "\nCorrect!\n"
                    fillAll(replaced, num, difficulty)
                else:
                    replaced[index] = word[:word.index(blank)] + answer + word[word.index(blank) + len(blank):]
                    print "\nCorrect!\n"
                    fillAll(replaced, num, difficulty)

# This function handles filling in all the remaining blanks of the same word once they've guessed the first instance correctly.
def fillAll(replaced, num, difficulty):
    index = -1
    for word in replaced:
        index += 1
        blank = "___{0}___".format(num)
        if blank in word:
            answer = setAnswer(difficulty, num)
            if blank == word:
                replaced[index] = answer
            else:
                replaced[index] = word[:word.index(blank)] + answer + word[word.index(blank) + len(blank):]

# This function sets the reference list of answers to pull from.
def setAnswer(difficulty, num):
    if difficulty == "easy":
        answer = e_key[num]
        return answer
    elif difficulty == "medium":
        answer = m_key[num]
        return answer
    elif difficulty == "hard":
        answer = h_key[num]
        return answer
    elif difficulty == "sample":
        answer = s_key[num]
        return answer
    else:
        print "Unexpected Result"
        answers.write(time.strftime("%c") + " | UR | setAnswer: " + difficulty + " " + num + "\n")

# This function handles checking whether the answer is PASS, True, or False.  False answers get logged in answers.txt
def guessing(num, difficulty):
    attempt = raw_input("\nWhat should be substituted for ___{0}___? > ".format(num))
    if attempt == "PASS":
        pass # TODO
    attempt = attempt.lower()
    if attempt == setAnswer(difficulty, num).lower():
        return True
    else:
        answers.write(time.strftime("%c") + " | {0}{1} | incorrect answer: ".format(difficulty[0], num) + attempt + "\n")
        return False

interface()

# TODO: Create PASS logic; Fix bug that causes some blanks not to be recognized, even when formatted exactly like other blanks that were recognized:  Seems to be based on punctuation next to ___#___, but the issues are inconsistent. (comma after E1 is okay, but comma after H1 is not recognized)

# python fill-in-the-blanks.py
