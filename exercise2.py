#counting days of week
fn = input('Enter file:')+'.txt'
fh = open(fn)

word_count = dict()
for line in fh:
    if line.startswith('From'):    #look for lines that start with "From"
        ll = line.split()
        if len(ll) > 2:             #look for the third word and keep a running count of each of the days of the week
            word_count[ll[2]] = word_count.get(ll[2],0)+1   
        
print(word_count)
fh.close()