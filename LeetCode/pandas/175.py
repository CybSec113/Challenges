#!/Users/jnn/Documents/Devel/Challenges/probenv/bin/python3

import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    result = pd.merge(person, address, on='personId', how='left')
    return result[['firstName', 'lastName', 'city', 'state']]

if __name__ == '__main__':
    data = [[1, 'Allen', 'Wang'], [2, 'Bob', 'Alice']]
    person = pd.DataFrame(data, columns=['personId', 'firstName', 'lastName']).astype({'personId':'Int64', 'firstName':'object', 'lastName':'object'})
    data = [[1, 2, 'New York City', 'New York'], [2, 3, 'Leetcode', 'California']]
    address = pd.DataFrame(data, columns=['addressId', 'personId', 'city', 'state']).astype({'addressId':'Int64', 'personId':'Int64', 'city':'object', 'state':'object'})

    print(combine_two_tables(person, address))