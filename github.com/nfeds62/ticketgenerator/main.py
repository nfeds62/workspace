from heightcheck import *
from agecheck import *
from ticketprice import *

def main():
    print("Welcome to the fair!")
    age = int(input("Enter your age: "))
    height = int(input("Enter your height in inches: "))
    if age_check(age) and heightcheck(height):
        print("You are old enough and tall enough to ride this ride.")
    else:
        print("You are not old enough or tall enough to ride this ride.")

    print(ticket_price(age))
main()