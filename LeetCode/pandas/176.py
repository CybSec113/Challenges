#!/Users/jnn/Documents/Devel/Challenges/probenv/bin/python3

import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    result = employee.drop_duplicates(subset='salary')[['salary']]
    result = result.nlargest(2, 'salary')
    result.columns = ['SecondHighestSalary']
    if result.empty or result.size == 1:
        result.loc[1, 'SecondHighestSalary'] = None
    return result.tail(1)

if __name__ == '__main__':
    data = [[1, 100], [2, 200], [3, 300]]
    employee = pd.DataFrame(data, columns=['id', 'salary']).astype({'id':'int64', 'salary':'int64'})
    print(second_highest_salary(employee))

    data = [[1, 100], [2, 100]]
    employee = pd.DataFrame(data, columns=['id', 'salary']).astype({'id':'int64', 'salary':'int64'})
    print(second_highest_salary(employee))

    data = [[1, 100]]
    employee = pd.DataFrame(data, columns=['id', 'salary']).astype({'id':'int64', 'salary':'int64'})
    print(second_highest_salary(employee))