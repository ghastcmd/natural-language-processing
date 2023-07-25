import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('../datasets/cyberbullying_tweets.csv')

data['comprimento'] = data['tweet_text'].apply(lambda x: len(x))

print("Comprimento dos tweets:")
print(data['comprimento'])

plt.hist(data['comprimento'], bins=60, edgecolor='black')
plt.xlabel('Comprimento tweet')
plt.ylabel('Frequência')
plt.title('Distribuição comprimento dos textos dos tweets')
plt.xlim(0, 800)
plt.savefig('dist.png')

plt.show()

