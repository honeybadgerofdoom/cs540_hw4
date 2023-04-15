# analysis.py
# -----------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


######################
# ANALYSIS QUESTIONS #
######################

# Set the given parameters to obtain the specified policies through
# value iteration.

def question2():
    return 0.9, 0.009

'''
answerDiscount: Closer to 1 -> cares more about future decisions
answerNoise: Chance that agent makes a random decision
answerLivingReward: Punishes agent for time
'''

def question3a():
    return 0.35, 0.009, -3

def question3b():
    return 0.5, 0.3, -1.5

def question3c():
    return 0.9, 0.01, -1.5

def question3d():
    return 0.9, 0.4, -1

def question3e():
    return 0.95, 0.001, 2

def question8():
    return 'NOT POSSIBLE'

if __name__ == '__main__':
    print('Answers to analysis questions:')
    import analysis
    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        print('  Question %s:\t%s' % (q, str(response)))
