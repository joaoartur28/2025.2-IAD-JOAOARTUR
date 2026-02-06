fname = input('Digite o nome do arquivo: ')
try:
    fh = open(fname)
except:
    print(f'Erro ao abrir o arquivo {fname}. Certifique-se que o arquivo existe.')
    exit()

counts = dict()
for line in fh:
    if line.startswith('From '):
        words = line.split()
        email = words[1]
        counts[email] = counts.get(email, 0) + 1

lst = list()
for email, count in counts.items():
    lst.append((count, email))

lst.sort(reverse=True)

top_count, top_email = lst[0]
print(f"{top_email} {top_count}")
