

code_map = {'trambulin':'lsls',
            'szia':'l',
            'gyere':'ll',
            'mizu':'sl',
            'siess':'sss',
}

def decode(string, cm):
	for key, value in code_map.items():
		if string == value:
			return key
	return 'kuku'

f = open('message.txt', 'r')
lines = []

for line in f.readlines():
	print(line)
	lines.append(line.strip())

t = ''
for line in lines:
	t = t + decode(line, code_map)
	t = t + ' '

print('*'*8)
print('The decoded message is:')
print('*'*8)
print(t)

