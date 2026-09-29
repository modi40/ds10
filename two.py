import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

transactions = [
    ['Video Lecture', 'Quiz'],
    ['Video Lecture', 'Assignment'],
    ['Quiz', 'Discussion Forum'],
    ['Video Lecture', 'Quiz', 'Assignment'],
    ['Assignment', 'Discussion Forum'],
    ['Video Lecture', 'Certificate'],
    ['Quiz', 'Certificate'],
    ['Video Lecture', 'Quiz'],
    ['Assignment', 'Certificate'],
    ['Video Lecture', 'Quiz', 'Certificate']
]

te = TransactionEncoder()
te_data = te.fit(transactions).transform(transactions)
df = pd.DataFrame(te_data, columns=te.columns_)

for support in [0.3, 0.4]:
    print("\nMinimum Support:", support)
    frequent_itemsets = apriori(df, min_support=support, use_colnames=True)
    print("\nFrequent Itemsets:")
    print(frequent_itemsets)
    rules = association_rules(frequent_itemsets, metric='confidence', min_threshold=0.5)
    print("\nAssociation Rules:")
    if len(rules) > 0:
        print(rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']])
    else:
        print("No association rules found.")
