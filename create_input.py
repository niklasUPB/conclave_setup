#!/usr/bin/python

import sys
import csv
import random


def write_half(lower,upper, writer):
    for x in range(lower,upper):
        line = []
        line.append( str(x) )
        for y in range(1,4):
            line.append(str( random.randint(0, 1000 )))
        writer.writerow(line)
def write_file(name, row, intersection , offset ):
    file = open(name , "w")
    writer = csv.writer(file)

    if name == "data/in1.csv":
       writer.writerow([ "primary_key", "name", "grade", "birthday"])
    if name == "data2/in2.csv":
       writer.writerow([ "primary_key", "books", "age", "money"])
    if name == "data3/in3.csv":
       writer.writerow([ "primary_key", "fun", "and", "games"])


    write_half(1,intersection, writer)
    write_half(intersection+offset, row+offset, writer)
    file.close()



if __name__ == "__main__":
    party1_row = sys.argv[1];
    party2_row = sys.argv[2];
    party3_row = sys.argv[3];
    intersection_size = sys.argv[4];
    write_file("data/in1.csv", int(party1_row) , int(intersection_size)  , 0 )
    write_file("data2/in2.csv", int(party2_row) , int(intersection_size) , int(party1_row) )
    write_file("data3/in3.csv", int(party3_row) , int(intersection_size) , int(party2_row) + int(party1_row  ) )





