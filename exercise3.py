#counting email address
fn = input('File name:')+'.txt'
fh = open(fn)

email_count = dict()
for line in fh:
    if line.startswith('From'):
        ll = line.split()
        email_count[ll[1]] = email_count.get(ll[1],0)+1

print(email_count)

maxi_count = None
maxi_email = None
for i in email_count:
    if maxi_count is None or maxi_count < email_count[i]:
        maxi_count = email_count[i]
        maxi_email = i

print(maxi_email, maxi_count)
fh.close()