"""plot graphs for paper"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn

df = pd.read_excel('data_for_paper.xlsx', index_col='Week')
plt.subplot(2, 1, 1)
df['Net production'].plot(label='original')
df['Reordered net production'].plot(label='rearranged', dashes=[5, 2, 5, 2])
plt.ylabel('Net production')
plt.legend(loc='lower center')
plt.title('Storage capacity calculation')
plt.subplot(2, 1, 2)
df['Storage'].plot(label='original')
df['Reordered storage'].plot(label='rearranged', dashes=[5, 2, 5, 2])
df['Minimum storage'].plot(label='minimum required', dashes=[2, 2, 2, 2])
plt.ylabel('Storage')
plt.legend(loc='lower center')
plt.tight_layout()
plt.savefig('plot.png')
plt.show()
