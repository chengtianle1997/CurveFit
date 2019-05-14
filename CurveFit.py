import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

u = 1299.3
f = 2445.4



#定义拟合函数
def func(x,b,p):
    return b * np.tan(p + np.arctan((u-x)/f))

def cfit(x,s):
        # 定义散点坐标
        x = [936.58, 958.24, 967.81, 991.26, 943.605]
        x = np.array(x)
        num = [2608.8, 2453.4, 2363.4, 2297.4, 2530.5]
        y = np.array(num)

        # 非线性最小二乘拟合
        popt, pcov = curve_fit(func, x, y)
        # 获取拟合参数
        print(popt)
        b = popt[0]
        p = popt[1]

        yvals = func(x, b, p)  # 拟合y值
        # 绘图
        plot1 = plt.plot(x, y, 's', label='original values')
        plot2 = plt.plot(x, yvals, 'r', label='polyfit values')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend(loc=4)  # 指定legend的位置右下角
        plt.title('curve_fit')
        plt.show()
        return popt

cfit(0,0)





