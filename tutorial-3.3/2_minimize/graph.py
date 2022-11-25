import matplotlib.pyplot as plt
import sys
sys.path.append("../../get_genesis_log")
import genesislog
(x,y)=genesislog.read_genesis("log", "POTENTIAL_ENE")
fig = plt.figure(figsize=(6,4))
ax = fig.add_subplot(111)
ax.grid()
ax.plot(x,y)
ax.set_xlabel("Steps", size=14)
ax.set_ylabel("Potential Energy (kcal/mol)",size=14)
plt.savefig("min.pdf")
plt.savefig("min.png")
quit()
