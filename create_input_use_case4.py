#!/usr/bin/python

import sys
import csv
import random


def write_half(start,amount, writer):
    for x in range(start, start+amount):
        line = []
        line.append( str(x) )
        line.append(str( random.randint(0, 1000 )))
        writer.writerow(line)
def write_file(name, row, intersection , start ):
    file = open(name , "w")
    writer = csv.writer(file)
    abstand = 1
    if name == "data/left.csv":
       writer.writerow([ "a", "b"])
    if name == "data2/left2.csv":
       writer.writerow([ "a", "b"])
       abstand = 2
    if name == "data/right.csv":
        writer.writerow(["c", "d"])
        abstand =3
    if name == "data/right2.csv":
        writer.writerow(["c", "d"])
        abstand =4
    write_half(start,intersection, writer)
    write_half(row * abstand, row-intersection , writer)
    file.close()



if __name__ == "__main__":
    rows =  int (sys.argv[1]);
    intersection_size = int((int(sys.argv[2])*0.5));
    half = int(int(rows) * 0.5)
    write_file("data/right.csv",  half, int(intersection_size), 0)
    write_file("data2/right2.csv", half, int(intersection_size),rows )
    write_file("data/left.csv", half, int(intersection_size), 0)
    write_file("data2/left2.csv", half, int(intersection_size),rows)
    file = open("Results/use_case4_local" , "a")
    writer = csv.writer(file)
    line = []
    line.append(rows)
    line.append(rows)
    writer.writerow(line)
    file.close()



