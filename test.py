import mizer

import sys, os

# disable
def disablePrint():
    sys.stdout = open(os.devnull, 'w')

# restore
def enablePrint():
    sys.stdout = sys.__stdout__

def getVariables_test1():
    test_var_str = "ABCD"
    test_var_list = ["A","B","C","D"]
    test_var_count = 4

    var_list, var_count = mizer.getVariables(test_var_str)

    print("getVariables_test1")
    result = True
    if var_list != test_var_list:
        print("FAILED: var_list != test_var_list")
        result = False

    if var_count != test_var_count:
        print("FAILED: var_count != test_var_count")
        result = False

    if result == True:
        print("PASSED")

def integerToBinaryString_test1():
    test_int = 7
    test_bits = 4
    test_binary_num = "0111"

    if mizer.integerToBinaryString(test_int, test_bits) != test_binary_num:
        print("Failed: ")

# test calls
getVariables_test1()
integerToBinaryString_test1()
