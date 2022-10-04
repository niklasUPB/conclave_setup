import sys
import json
import timeit

from conclave.comp import TrustSetPropDown
from conclave.lang import *
from conclave.utils import *
from conclave import workflow

from time import gmtime, strftime

"""
def protocol():
    cols_in_left = [defCol("a", "INTEGER", 1,2), defCol("b", "INTEGER", 1)]#ab
    cols_in_right = [defCol("a", "INTEGER",  1,2), defCol("d", "INTEGER", 2)]#cw
    cols_in_left2 = [defCol("e", "INTEGER", 1,2), defCol("f", "INTEGER", 1)]#ab
    cols_in_right2 = [defCol("g", "INTEGER", 1,2), defCol("h", "INTEGER", 2)]#yu
    left = create("left", cols_in_left, {1})
    right = create("right", cols_in_right, {2})
    right2 = create("right2", cols_in_right2, {2})
    left2 = create("left2", cols_in_left2, {1})
    first_concat = concat([left, right] ,  "first_concat" , ["a", "test"]  )# a!,b
    second_concat = concat([left2, right2] ,  "second_concat" , ["i" ,"r"]   )#ir
    Join = join( first_concat , second_concat, "Join", ["a"], ["i"] )#ai

    #join_result = join(input_1, input_2, 'join_result', ['a'], ['c'])
    collect(Join, 1)
    collect(Join, 2)

    return { left, right,right2, left2 }
"""
def protocol():
    cols_in_left = [defCol("a", "INTEGER", 1,2), defCol("b", "INTEGER", 1)]#ab
    cols_in_right = [defCol("c", "INTEGER",  1,2), defCol("d", "INTEGER", 1)]#cw
    cols_in_left2 = [defCol("a", "INTEGER", 1,2), defCol("b", "INTEGER", 2)]#ab
    cols_in_right2 = [defCol("c", "INTEGER", 1,2), defCol("d", "INTEGER", 2)]#yu
    left = create("left", cols_in_left, {1})
    right = create("right", cols_in_right, {1})
    right2 = create("right2", cols_in_right2, {2})
    left2 = create("left2", cols_in_left2, {2})
    first_concat = concat([right2, right] ,  "first_concat"  )# a!,b
    second_concat = concat([left2, left] ,  "second_concat"    )#ir
    Join = join( first_concat , second_concat, "Join", ["c"], ["a"] )#ai

    #join_result = join(input_1, input_2, 'join_result', ['a'], ['c'])
    collect(Join, 1)
    collect(Join, 2)

    return { left, right,right2, left2 }



if __name__ == "__main__":
    with open(sys.argv[1], "r") as c:
        c = json.load(c)
    workflow.run(protocol, c, mpc_framework="jiff", apply_optimisations=True)
    

