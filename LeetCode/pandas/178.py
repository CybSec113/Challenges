#!/Users/jnn/Documents/Devel/Challenges/probenv/bin/python3

import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    result = scores.sort_values(by='score', ascending=False)
    result['rank'] = result['score'].rank(method='dense', ascending=False).astype('int64')
    return result[['score', 'rank']]

if __name__ == '__main__':
    data = [[1, 3.5], [2, 3.65], [3, 4.0], [4, 3.85], [5, 4.0], [6, 3.65]]
    scores = pd.DataFrame(data, columns=['id', 'score']).astype({'id':'Int64', 'score':'Float64'})
    print(order_scores(scores))
