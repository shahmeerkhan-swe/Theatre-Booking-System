#Khan_Shahmeer December 2022 CA-07

import math
import random

global prod_cost
global band_A
global band_B


prod_cost = int(input("Enter the production cost of the show: "))
band_A = int(input("Enter the price of a seat in Band A (Double of price of Band B): "))
band_B = int(input("Enter the price of a seat in Band B (Half of price of Band A): "))


def full_house():

    band_A_full = band_A * 10
    band_B_full = band_B * 10

    revenue_full = band_A_full + band_B_full
    break_even_full = prod_cost/revenue_full

    print("\nFull House Revenue: ")
    print("Band-A: 10 seats at",band_A, "$ per seat:", band_A_full)
    print("Band-B: 10 seats at",band_B, "$ per seat:", band_B_full)
    print("Revenue: Total for one full house: ", revenue_full)
    print("Number of shows to break even: ", math.ceil(break_even_full))

    return

def part_house():

    band_A_seats = random.randint(1,10)
    band_B_seats = random.randint(1,10)

    band_A_part = band_A * band_A_seats
    band_B_part = band_B * band_B_seats

    revenue_part = band_A_part + band_B_part
    break_even_part = prod_cost/revenue_part

    print("\nPart-house revenue: ")
    print("Band A:",band_A_seats,"seats at",band_A,"$ per seat:", band_A_part)
    print("Band B:", band_B_seats, "seats at", band_B, "$ per seat:", band_B_part)
    print("Revenue: Total for one part house: ", revenue_part)
    print("Number of shows to break even: ", math.ceil(break_even_part))

    return

def seating_table():
    seating_area = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
    for row in seating_area:
        for column in row:
            print(column,end = " ")
        print()
    return

def main():
    print("\nThe seating arrangement for tonight's show:")
    seating_table()
    print("\nProduction Cost: ",prod_cost)
    full_house()
    part_house()

main()
