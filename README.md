# Fill-In-The-Blanks
Another Udacity Project: a Fill In The Blanks Quiz

The fill-in-the-blanks quiz is almost feature complete and bug free.  There's a fill-in-the-blanks.pyc file in here which is a compiled version of this project to demonstrate how the project should function.  The file I created is the fill-in-the-blanks.py file.  I also created a file called answers.txt to accompany the quiz; when someone submits an incorrect answer, it logs the answer and relevant details for training and troubleshooting, plus it catches a few Unexpected Results showing some details that could help diagnose if things don't function as expected.

The instructions mention the ability to type in "PASS" to skip that blank and come back to it later, but I will build that feature next, ignore for now.

Also, I am troubleshooting a bug that doesn't recognize some of the blanks even when they are formatted exactly the same as other blanks that are recognized (causing the program to declare victory prematurely).  My temporary work around are to put a space before and after the problematic blanks.  They're recognized, but don't look right.  The answers.txt log contains some printouts of the paragraphs split into lists of individual words, which the program uses to cycle through looking for blanks.  You may notice that some of the blanks that had issues getting recognized look exactly the same as blanks that did not have that issue.  For comparison purposes, I put an "!" at the end of each printout for the paragraphs that were able to successfully run through to the end reading each blank.

I realize that the current state of this program is probably good enough to pass the Stage 2 project per requirements, but since it's a learning project, I really want to understand and squash this bug, without needing a workaround.  And while the PASS feature is out of the scope of the project, I like the challenge to see if I can implement it simply enough.
