import os
import sys

try:
    FILENAME = sys.argv[1] 
    TESTCASE = 5
    INPUT_PATH = "./"
    if len(sys.argv)>=3:
        TESTCASE = int(sys.argv[2])
    if len(sys.argv)>=4:
        INPUT_PATH = sys.argv[3]
    
except (Exception):
    print("pls add <file name> <no. of testcase> <path to testcase>{")
    print("ex -> python tester.py 11_add.c 1 testcase")
    exit()

def make_output():
    os.system(f"gcc {FILENAME} -o {FILENAME}.out")
    for i in range(1,TESTCASE+1):
        #os.system(f"./{FILENAME}.out < {i}.in > test_{i}.out.tmp")
        os.system(f"./{FILENAME}.out < {INPUT_PATH}/{i}.in")

def clear_output():
    for i in range(1,TESTCASE+1):
        os.system(f"rm test_{i}.out.tmp")
    os.system(f"rm {FILENAME}.out")
"""
def check_output(id):
    result = []
    for i in range(1,TESTCASE+1):
        std_output = open(f"std{id:02d}_{i}.out.tmp",'r').read().strip()
        print(f"Testcase {i}")
        print("STD output   :",std_output)
        if std_output == ANS[i-1]:
            result.append('P')
        elif std_output.replace(' ','') == ANS[i-1].replace(' ',''):
            result.append('S')
        else:
            result.append('-')
            print("Answer       :",ANS[i-1])
        print("...........................................")
    for i in result:
        print(i,end='')
    print()
"""
make_output()
#clear_output()