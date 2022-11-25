import matplotlib.pyplot as plt
x=[]
y=[]
f = open('output.rms','r')
for line in f:
    data = line[:-1].split()
    x.append(float(data[0]))
    y.append(float(data[1]))
f.close()
fig = plt.figure(figsize=(6,4))
ax = fig.add_subplot(111)
ax.grid()
ax.plot(x,y)
ax.set_xlabel("Frames", size=14)
ax.set_ylabel("RMSD (Angstrom)",size=14)
plt.savefig("rmsd_out.pdf")
plt.savefig("rmsd_out.png")
quit()
