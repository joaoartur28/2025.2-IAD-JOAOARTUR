import sys

fname = input('Digite o nome do arquivo: ')
try:
    fh = open(fname)
except FileNotFoundError:
    print(f'Erro ao abrir o arquivo {fname}. Certifique-se de que o arquivo existe.')
    sys.exit()

counts = dict()
for line in fh:
    if line.startswith('From '):
        words = line.split()
        time_str = words[5]
        hour = time_str.split(':')[0]
        counts[hour] = counts.get(hour, 0) + 1

lst = list()
for hour, count in counts.items():
    lst.append((hour, count))

lst.sort()

for hour, count in lst:
    print(f"{hour} {count}")
