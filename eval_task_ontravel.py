import argparse

parser = argparse.ArgumentParser()
parser.add_argument('first_file')
parser.add_argument('second_file')
args = parser.parse_args()

first_file = open(args.first_file, 'r')
second_file = open(args.second_file, 'r')
third_file = open('out.txt', 'w')

first_file_lines = first_file.readlines()
second_file_lines = second_file.readlines()

restaraunts = dict()

for line in second_file_lines:
    line_split = line.split(' ', 1)
    restaraunts[int(line_split[0])] = line_split[1].rstrip()

answer = list()

for line in first_file_lines:
    line_split = line.split(' ', 1)
    answer.append(line_split[0])
    if len(line_split) == 1:
        continue

    restaraunt_numbers = line_split[1].split(',')
    
    answer.append(' ')
    answer.append(restaraunts[int(restaraunt_numbers[0])])

    for i in range(1, len(restaraunt_numbers)):
        answer.append(', ')
        answer.append(restaraunts[int(restaraunt_numbers[i])])

    answer.append('\n')

answer.pop()
third_file.write("".join(answer))
    
