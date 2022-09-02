# coding=utf8
import sys
import json
from conclave.lang import *
from conclave.utils import *
from conclave import workflow


def protocol():

	cols_in_one = [
		defCol("primary_key", "INTEGER", [1]),
		defCol("name", "INTEGER", [1]),
		defCol("grade", "INTEGER", [1]),
		defCol("birthday", "INTEGER", [1]),
	]
	in1 = create("in1", cols_in_one, {1})

	cols_in_two = [
		defCol("primary_key", "INTEGER", [2]),
		defCol("books", "INTEGER", [2]),
		defCol("age", "INTEGER", [2]),
		defCol("money", "INTEGER", [2])
	]
	in2 = create("in2", cols_in_two, {2})
	cols_in_three = [
		defCol("primary_key", "INTEGER", [3]),
		defCol("fun", "INTEGER", [3]),
		defCol("and", "INTEGER", [3]),
		defCol("games", "INTEGER", [3])
	]
	in3 = create("in3", cols_in_three, {3})

	join1 = join(in1, in2, 'join1', ['primary_key'], ['primary_key'])
	
	collect(join1, 3)
	
	return {in1, in2}


if __name__ == "__main__":

	with open(sys.argv[1], "r") as c:
		c = json.load(c)

	workflow.run(protocol, c, mpc_framework="jiff", apply_optimisations=True)
