from http.client import NO_CONTENT
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer


def datasets_demo():
    """sklearn 数据集使用"""

    # 获取数据集
    iris = load_iris()
    print("鸢尾花数据集: \n", iris)
    print("查看数据集描述:\n", iris["DESCR"])
    print("查看特征值的名字:\n", iris.feature_names)
    print("查看特征值: \n", iris.data, iris.data.shape)

    # 数据集划分
    x_train, x_test, y_train, y_test = train_test_split(
        iris.data, iris.target, test_size=0.25, random_state=22)
    print("训练集的特征值: \n", x_train, x_train.shape)

    return None


def dict_demo():
    """字典特征抽取"""
    data = [{'city': '北京', 'temperature': 100},
            {'city': '上海', 'temperature': 60}]
    # 1. 实例化一个转换器类
    transfer = DictVectorizer(sparse=False)

    # 2. 调用 fit_transform()
    data_new = transfer.fit_transform(data)
    print("data_new:\n", data_new)

    return NO_CONTENT


# datasets_demo()
dict_demo()
