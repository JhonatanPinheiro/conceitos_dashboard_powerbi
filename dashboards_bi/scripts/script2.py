import matplotlib.pyplot as plt
import seaborn as sns

sns.violinplot(x=dataset["Country"],y=dataset["Units"] )
plt.show()