import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler


def recommend(raw_data):
    raw_data = list(raw_data)

    output = ''
    if int(raw_data[0]) == 0:
        output += '10'
    else:
        output += '01'

    for idx in range(5):
        if idx == int(raw_data[1]):
            output += '1'
            continue
        output += '0'

    if int(raw_data[2]) == 0:
        output += '10'
    else:
        output += '01'

    for idx in range(5):
        if idx == int(raw_data[3]):
            output += '1'
            continue
        output += '0'

    '''
    Made a dummy

    raw_data[0]
    0 - FEMALE
    1 - MALE

    raw_data[1]
    0 - 20대
    1 - 30대
    2 - 40대
    3 - 50대
    4 - 60대

    raw_data[2]
    0 - 기혼
    1 - 미혼

    raw_data[3]
    0 - 갓
    1 - 고급
    2 - 중급
    3 - 프리
    4 - 학생
    '''

    output = np.array(list(output))

    train_list = list()
    for train_data in ['train_' + alphabet + '.csv' for alphabet in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')]:
        train_list.append(pd.read_csv(train_data))

    param_list = [[4, 5, 2], [1, 5, 2], [7, 10, 2], [6, 9, 2], [3, 5, 2], [6, 5, 20], [6, 7, 2], [4, 19, 2]]

    score = list()

    for idx, param in enumerate(param_list):
        tree = DecisionTreeClassifier(max_depth=param[0], min_samples_leaf=param[1], min_samples_split=param[2])
        train_data = train_list[idx]
        x = pd.get_dummies(train_data.drop('choice1', axis=1, inplace=False))
        y = train_data[['choice1']]
        tree.fit(x, y)
        to_be = tree.predict(output.reshape(1, -1))[0]

        if ((output[0] == '0') and ((idx == 2) or (idx == 3) or (idx == 4))):
            to_be = 0
        if ((output[0] == '1') and ((idx == 0) or (idx == 6) or (idx == 7))):
            to_be = 0

        score.append(to_be)

    return score

