import argparse

parser = argparse.ArgumentParser("description= previous_num and current_number")
parser.add_argument("--current_number")
parser.add_argument("--previous_number")

args = parser.parse_args()
previous_num = int(args.previous_number)
current_num = int(args.current_number)
for i in range(10):
     total = previous_num + i
     print(f'Current number {i} Previous Number {previous_num} is {total}')
     previous_num = i
