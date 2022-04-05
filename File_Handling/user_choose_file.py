fname = input('Enter the file name: ')
fhand = open(fname)

count = 0

for line in fhand:
    if line.startswith('Subject:'):
        count += 1
        
print('There are', count, 'subject lines in', fname)