"""
Common utilities and constants for DAA Assignment 2 (CO2)
Student: P Sai Deepak
Registration Number: 192411047
Seed: 1047 (Last 4 digits of Registration Number)
"""

import datetime
import random

STUDENT_NAME = "P Sai Deepak"
REG_NO = "192411047"
SEED = 1047

def print_header(title="ALGORITHM EXECUTION BENCHMARK"):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    bar = "=" * 76
    print(bar)
    print(f" REGISTRATION NO : {REG_NO:<16} | STUDENT NAME : {STUDENT_NAME}")
    print(f" MODULE / TOPIC  : DAA ASSIGNMENT 2 (CO2 - Brute Force and Exhaustive Search)")
    print(f" EXECUTION TIME  : {timestamp:<16} | RANDOM SEED  : {SEED}")
    print(f" TASK / CONTEXT  : {title}")
    print(bar)

def set_seed(offset=0):
    random.seed(SEED + offset)
