import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

data = pd.read_excel('./pokemons.xlsx')
print(data)

#Matpotlib visualization 1 
plt.figure(figsize=(8, 6))
plt.bar(data['Name'], data['Attack'])
plt.xlabel('Name')
plt.ylabel('Attack')
plt.title('Bar graph')
plt.xticks(rotation=45)
plt.savefig('pokemons_attacks.png')

#Matpotlib visualization 2
plt.figure(figsize=(8, 6))
plt.plot(data['Name'], data['Defense'], marker='o')
plt.xlabel('Name')
plt.ylabel('Defense')
plt.title('Line chart')
plt.xticks(rotation=45)
plt.savefig('pokemons_defense.png')

# decorated bar chart
plt.figure(figsize=(8, 6))
sns.set_palette('pastel')
sns.barplot(data=data, x='Name', y='HP')
plt.xlabel('Name')
plt.ylabel('HP')
plt.title('decorated bar chart')
plt.xticks(rotation=45)
plt.savefig('decorated_bar_chart.png')
plt.show()

# violon plot
plt.figure(figsize=(8, 6))
sns.violinplot(data=data, x='Name', y='HP')
plt.xlabel('Name')
plt.ylabel('HP')
plt.title('Violin plot')
plt.xticks(rotation=45)
plt.savefig('violinplot.png')
plt.show()

# worldcloud visualization
wordcloud_data = ' '.join(data['Name'])
wordcloud = WordCloud(width=800, height=600, background_color='white').generate(wordcloud_data)
plt.figure(figsize=(8, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('wordcloud')
plt.savefig('worldcloud.png')
plt.show()