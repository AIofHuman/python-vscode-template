import os

import numpy as np  # type: ignore
import pandas as pd  # type: ignore


def create_test_csv(file_name='test.csv') -> None:
    """Create the test csv file from pandas dataframe object

    Args:
        file_name (str, optional): name of the csv file. Defaults to 'test.csv'.
    """
    current_path = os.curdir
    array = np.zeros((1, 2))
    df = pd.DataFrame(data=array)
    df.to_csv(current_path + '/' + file_name)
    print('test csv file created')
    print(
        'veryyyyyyyyyyyyyyyyyyyyyyyyyyy long string priningggggggggggggggggggg'
    )


if __name__ == '__main__':
    create_test_csv()
    print('test done')
