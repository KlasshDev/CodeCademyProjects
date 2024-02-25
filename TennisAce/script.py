import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# load and investigate the data here:
df = pd.read_csv('tennis_stats.csv')
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_seq_items', None)
pd.set_option('display.max_colwidth', 500)
pd.set_option('expand_frame_repr', True)
print(df.head())

print("\ninfo()")
print(df.info())

print('\nDescribe()')
print(df.describe())


# perform exploratory analysis here:



# Some visualizations to see sparse connections

plt.style.use(['dark_background'])




## Chart a few options to get visual

#for value in df.columns:
#    plt.scatter(df[value], df['Winnings'])
#    plt.ticklabel_format(style='plain', axis='y')
#    plt.xticks(rotation=45)
#    plt.xlabel(value)
#    plt.ylabel("Winnings")
#    plt.show()
featureList = [
'FirstServePointsWon'
,'FirstServeReturnPointsWon'
,'Aces'
,'BreakPointsFaced'
,'BreakPointsOpportunities'
,'DoubleFaults'
,'ReturnGamesPlayed'
,'ReturnPointsWon'
,'ServiceGamesPlayed'
,'ServiceGamesWon'
,'Wins'
,'Ranking']

## perform single feature linear regressions here:
print(featureList)
features = df[['FirstServePointsWon']]
winnings = df[['Winnings']]

feature_train, feature_test, winnings_train, winnings_test = \
        train_test_split(features, winnings, train_size = 0.8)

        
model = LinearRegression()
model.fit(feature_train, winnings_train)

#Score Model on test data
print('Predicting Winnings with FirstServePointsWon Test Score:', \
        model.score(feature_test, winnings_test))

winnings_prediction = model.predict(feature_test)

plt.scatter(winnings_test, winnings_prediction, alpha=0.4)
plt.title('Predicted Winnings vs. Actual Winnings - 1 Feature')
plt.xlabel('Actual Winnings')
plt.ylabel('Predicted Winnings')
plt.ticklabel_format(style='plain', axis='x')
plt.xticks(rotation=45)

plt.show()
plt.clf()



## perform two feature linear regressions here:





## perform multiple feature linear regressions here:
features = df[featureList]
winnings = df[['Winnings']]

feature_train, feature_test, winnings_train, winnings_test = \
        train_test_split(features, winnings, train_size = 0.8)

        
model = LinearRegression()
model.fit(feature_train, winnings_train)

#Score Model on test data
print('Predicting Winnings with Multiple Features Test Score:', \
        model.score(feature_test, winnings_test))

winnings_prediction = model.predict(feature_test)

plt.scatter(winnings_test, winnings_prediction, alpha=0.4)
plt.title('Predicted Winnings vs. Actual Winnings - Multiple Features')
plt.xlabel('Actual Winnings')
plt.ylabel('Predicted Winnings')
plt.ticklabel_format(style='plain', axis='x')
plt.xticks(rotation=45)

plt.show()
plt.clf()

