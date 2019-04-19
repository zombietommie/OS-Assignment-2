# Tommy Tran 
# 2420005
# CSCI 4401 - OS
# Assignment 2 - Quesiton 2

# imports
import threading
import random
import time

class Philosopher(threading.Thread):

    # This starts off the program as active, time for dinner
    active = True

    # constructor
    def __init__(self, name, leftFork, rightFork):
        threading.Thread.__init__(self)
        self.name = name
        self.leftFork = leftFork
        self.rightFork = rightFork

    # Fork checks; basically starts the check 
    # with the left hand first 
    # if the left is obtainable 
    # take the fork and check for the right
    # if there is a right take it and eat
    # If left is not available then stop 
    # and go on to the next person
    # if the right is not available then 
    # stop and drop the left fork
    def Fork(self):
        fork1, fork2 = self.leftFork, self.rightFork
        while(self.active):
            currentTime = time.sleep(.01)
            milliTime = currentTime * 1000
            print('%s, Time: %f ms, entering hungry state' % self.name,milliTime)

            # left fork check first
            fork1.acquire(True)
            print('%s, Time: %f picked up fork %d' % self.name, milliTime, fork1)
            lock = fork2.acquire(False)
            print('%s, Time: %f tried to pick up fork %d, it\'s unavailable' % self.name, milliTime, fork2)
            if lock: break
            fork1.release()
        else:
            return

        self.Eat(milliTime)
        fork2.release()
        fork1.release()

    def Eat(self,milliTime):
        eatTime = time.sleep(random.uniform(.01, .04))
        milliEat = eatTime * 1000
        print('%s, Time: %f entering eating state. Will eat for %f', self.name, milliTime, milliEat)

def DiningPhilosophers():
    forks = [threading.Lock() for n in range(4)]
    persons = ('Philosopher 0', 'Philosopher 1', 'Philosopher 2', 'Philosopher 3')
    philosophers = [Philosopher(persons[i], forks[i - 1], forks[(i + 2) % 4])
    \
            for i in range(4)]
    
    Philosopher.active = True
    for p in philosophers: p.start()
    time.sleep(60)
    Philosopher.running = False
    print('Dinner Completed!')

DiningPhilosophers()