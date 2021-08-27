#counting domain name
fn = input('File name:')+'.txt'
fh = open(fn)

domain_count = dict()
for line in fh:
    if line.startswith('From:'):
        ll = line.split()
        domain = ll[1].split('@')[1]
        domain_count[domain] = domain_count.get(domain,0)+1

print(domain_count)
fh.close()