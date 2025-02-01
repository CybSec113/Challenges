#!/Users/jnn/Documents/Devel/Challenges/probenv/bin/python3

import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    result = employee.drop_duplicates(subset='salary')[['salary']]
    result = result.nlargest(N, 'salary')
    result.columns = [f"getNthHighestSalary({N})"]
    if result.empty or result.size < N:
        result.loc[N-1, f"getNthHighestSalary({N})"] = None
    print(result)
    return result.tail(1)

if __name__ == '__main__':
    data = [[1, 100], [2, 200], [3, 300]]
    employee = pd.DataFrame(data, columns=['id', 'salary']).astype({'id':'int64', 'salary':'int64'})
    print(nth_highest_salary(employee, 10))

    data = [[1, 100], [2, 200]]
    employee = pd.DataFrame(data, columns=['id', 'salary']).astype({'id':'int64', 'salary':'int64'})
    print(nth_highest_salary(employee, 3))

    data = [[1, 100]]
    employee = pd.DataFrame(data, columns=['id', 'salary']).astype({'id':'int64', 'salary':'int64'})
    print(nth_highest_salary(employee, 2))