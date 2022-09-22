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

    if name == "data/input_1.csv":
       writer.writerow([ "primary_key", "user_data1_party1", "user_data2_party1", "user_data3_party1"])
    if name == "data2/input_2.csv":
       writer.writerow([ "primary_key", "user_data1_party2", "user_data2_party2", "user_data3_party2"])



    write_half(1,intersection, writer)
    write_half(intersection+offset, row+offset, writer)
    file.close()



if __name__ == "__main__":
    party1_row = sys.argv[1];
    party2_row = sys.argv[2];
    intersection_size = sys.argv[3];
    write_file("data/input_1.csv", int(party1_row) , int(intersection_size)  , 0 )
    write_file("data2/input_2.csv", int(party2_row) , int(intersection_size) , int(party1_row) )
    file = open("Results/use_case1_local" , "a")
    writer = csv.writer(file)
    line = []
    line.append(party1_row)
    line.append(party2_row)
    writer.writerow(line)
    file.close()



