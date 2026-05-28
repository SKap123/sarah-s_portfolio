#Sarah
#Scandal: Print the two months where the influencer had a scandal that caused them to have no revenue leading to their downfall
#Initialize
import pandas as pd
data = pd.read_csv('influencer.csv')
month = data["Month"].tolist()
views = data["Views"].tolist()
dislikes = data["Dislikes"].tolist()
subs = data["Subscriber(+-)"].tolist()
revenue = data["Revenue"].tolist()
filter = []
#Functions
def influencer_finder(check, score):
    for i in range (len(month)):
        if check[i] <= score:
            filter.append([i])
    print(filter)
    filter.clear()
#Main
influencer_finder(revenue, 0)
print(data.loc[[98,107]])
