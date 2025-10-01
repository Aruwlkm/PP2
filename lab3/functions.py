import math
import random
from itertools import permutations
def grams_to_ounces(grams):
    return 28.3495231 * grams

def fahrenheit_to_celsius(F):
    return (5/9) * (F - 32)

def solve(numheads, numlegs):
    for chickens in range(numheads+1):
        rabbits = numheads - chickens
        if 2*chickens + 4*rabbits == numlegs:
            return chickens, rabbits
    return None, None

def filter_prime(numbers):
    return [n for n in numbers if is_prime(n)]

def all_permutations(s):
    return [''.join(p) for p in permutations(s)]

def reverse_words(s):
    return ' '.join(s.split()[::-1])

def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

def spy_game(nums):
    code = [0,0,7]
    for n in nums:
        if n == code[0]:
            code.pop(0)
        if not code:
            return True
    return False

def volume_sphere(r):
    return (4/3) * math.pi * (r**3)

def unique_list(lst):
    new = []
    for x in lst:
        if x not in new:
            new.append(x)
    return new

def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

def histogram(lst):
    for n in lst:
        print('*' * n)

def guess_game():
    name = input("Hello! What is your name?\n")
    number = random.randint(1,20)
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    tries = 0
    while True:
        guess = int(input("Take a guess.\n"))
        tries += 1
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {tries} guesses!")
            break