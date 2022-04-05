fname = input('Enter the file name: ')

try:
    fhand = open(fname)
except:
    print('File', fname, 'can not be opened.')
    exit()
    
count = 0
for line in fhand:
    if line.startswith('Subject:'):
        count += 1
        
print('There are', count, 'subject lines in', fname)