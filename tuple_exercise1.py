#dictionary {address:count}
file_name = input('File name: ')+'.txt'
fh = open(file_name)

addresses = {}
for line in fh:
    if line.startswith('From'):
        email = line.split()[1]
        addresses[email] = addresses.get(email,0)+1

tmp = sorted(addresses.items(), key=lambda x:x[1], reverse=True)

max_address, max_count = tmp[0][0],tmp[0][1]
print(max_address, max_count)

fh.close()