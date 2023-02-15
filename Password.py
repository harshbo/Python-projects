import random
l = "abcdefghijklmnopqrstuvwxyz"
u = l.upper();
n ="1234567890"
s = "!@#$%^&*()_+=-}{\/?:;[]<>,."
all = l+u+n+s
length = 8
password = "".join(random.sample(all,length))
print("Suggested Password : ", password);
