'''
PART ONE
'''

with open('input.txt') as file:
# with open('test.txt') as file:
    lines = file.readlines()
gamma = ""
epsilon = ""

for x in zip(*lines):
    if x.count('0') > x.count('1'):
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"

print(int(gamma, 2) * int(epsilon, 2))

'''
PART TWO
'''

most = lines[:]
for i in range(len(lines[0])):
    bits = list(zip(*most))[i]
    if len(most) == 1:
        break
    if bits.count('0') > bits.count('1'):
        most = [line for line in most if line[i] == '0']
    else:
        most = [line for line in most if line[i] == '1']
    
o2 = int(most[0], 2)

least = lines[:]
for i in range(len(lines[0])):
    bits = list(zip(*least))[i]
    if len(least) == 1:
        break
    if bits.count('1') < bits.count('0'):
        least = [line for line in least if line[i] == '1']
    else:
        least = [line for line in least if line[i] == '0']

co2 = int(least[0], 2)

print(o2 * co2)