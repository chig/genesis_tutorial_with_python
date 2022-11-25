import matplotlib.pyplot as plt
import sys
sys.path.append("../scripts/get_genesis_log")
import genesislog
(x,y)=genesislog.read_genesis("log2", "BOXX")
fig = plt.figure(figsize=(6,4))
ax = fig.add_subplot(111)
ax.grid()
ax.plot(x,y)
ax.set_xlabel("Steps", size=14)
ax.set_ylabel("BOXX (Angstrom)",size=14)
plt.savefig("log2_box.pdf")
plt.savefig("log2_box.png")
quit()
