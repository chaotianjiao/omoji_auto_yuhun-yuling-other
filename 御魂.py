from icecream import ic
from basic_function import basic


if __name__ == '__main__':
    # 可更改右边的数值设定要刷的次数
    for i in range(1, 1000):
        # 依据每个人御魂耗时不同，请自行设定use_time,建议比完成时间大8~10秒
        basic(use_time=48, path='./resource/御魂按钮.png')
        # 显示已经刷了多少次
        ic(i)



