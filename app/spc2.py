#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy



CHART_X_BAR_R_X = "Xbar R - X"
CHART_X_BAR_R_R = "Xbar R - R"
CHART_X_BAR_S_X = "Xbar S - X"
CHART_X_BAR_S_S = "Xbar S - S"
CHART_X_MR_X = "X mR - X"
CHART_X_MR_MR = "X mR - mR"
CHART_P = "p"
CHART_NP = "np"
CHART_C = "c"
CHART_U = "u"
CHART_EWMA = "EWMA"
CHART_CUSUM = "CUSUM"
CHART_THREE_WAY = "three way"
CHART_TIME_SERIES = "time series"

# RULES_1_BEYOND_3SIGMA = "1 beyond 3*sigma,一个点远离中心线超过3倍标准差"
# RULES_2_OF_3_BEYOND_2SIGMA = "2 of 3 beyond 2*sigma，连续3个点，有2个点远离中心线2倍标准差"
# RULES_4_OF_5_BEYOND_1SIGMA = "4 of 5 beyond 1*sigma，连续5个点，有4个点远离中心线1倍标准差"
# RULES_7_ON_ONE_SIDE = "7 on one side，连续7个点在同一侧"
# RULES_8_ON_ONE_SIDE = "8 on one side，连续8个点在同一侧"
# RULES_9_ON_ONE_SIDE = "9 on one side，连续9个点在同一侧"
# RULES_6_TRENDING = "6 trending，连续6个点持续上升或下降，可能设备磨损"
# RULES_14_UP_DOWN = "14 up down，14个点交互升降，如此整齐的数据有没有可能作假？"
# RULES_15_BELOW_1SIGMA = "15 below 1*sigma，连续15点在中心线在1倍标准差之内"
# RULES_8_BEYOND_1SIGMA_BOTH_SIDES = "8 beyond 1*sigma on both sides，连续8点在中心线的1倍标准差之外"


RULES_1_BEYOND_3SIGMA = "1个点远离中心线超过3倍标准差"
RULES_2_OF_3_BEYOND_2SIGMA = "连续3个点，有2个点远离中心线2倍标准差"
RULES_4_OF_5_BEYOND_1SIGMA = "连续5个点，有4个点远离中心线1倍标准差"
RULES_7_ON_ONE_SIDE = "连续7个点在同一侧"
RULES_8_ON_ONE_SIDE = "连续8个点在同一侧"
RULES_9_ON_ONE_SIDE = "连续9个点在同一侧"
RULES_6_TRENDING = "连续6个点持续上升或下降，可能设备磨损"
RULES_14_UP_DOWN = "14个点交互升降，如此整齐的数据有没有可能作假？"
RULES_15_BELOW_1SIGMA = "连续15点在中心线在1倍标准差之内"
RULES_8_BEYOND_1SIGMA_BOTH_SIDES = "连续8点在中心线的1倍标准差之外"



RULES_BASIC = [RULES_1_BEYOND_3SIGMA, 
               RULES_7_ON_ONE_SIDE,
               RULES_2_OF_3_BEYOND_2SIGMA,
               RULES_4_OF_5_BEYOND_1SIGMA,
               RULES_9_ON_ONE_SIDE,
               RULES_6_TRENDING,
               RULES_14_UP_DOWN,
               RULES_15_BELOW_1SIGMA,
               RULES_8_BEYOND_1SIGMA_BOTH_SIDES,
               RULES_8_ON_ONE_SIDE]
RULES_WECO = [RULES_1_BEYOND_3SIGMA,
              RULES_2_OF_3_BEYOND_2SIGMA, 
              RULES_4_OF_5_BEYOND_1SIGMA, 
              RULES_8_ON_ONE_SIDE,
              RULES_6_TRENDING, RULES_14_UP_DOWN]
RULES_NELSON = [RULES_1_BEYOND_3SIGMA,
                RULES_9_ON_ONE_SIDE,
                RULES_6_TRENDING,
                RULES_14_UP_DOWN,
                RULES_2_OF_3_BEYOND_2SIGMA,
                RULES_4_OF_5_BEYOND_1SIGMA,
                RULES_15_BELOW_1SIGMA,
                RULES_8_BEYOND_1SIGMA_BOTH_SIDES]

RULES_ALL = [RULES_1_BEYOND_3SIGMA,
             RULES_2_OF_3_BEYOND_2SIGMA,
             RULES_4_OF_5_BEYOND_1SIGMA,
             RULES_7_ON_ONE_SIDE,
             RULES_8_ON_ONE_SIDE,
             RULES_6_TRENDING,
             RULES_14_UP_DOWN,
             RULES_15_BELOW_1SIGMA,
             RULES_8_BEYOND_1SIGMA_BOTH_SIDES]


def test_beyond_limits(data, center, lcl, ucl):
    return data[0] > ucl or data[0] < lcl

def test_violating_runs(data, center, lcl, ucl):
    for i in range(1, len(data)):
        if (data[i-1] - center)*(data[i] - center) < 0:
            return False
    return True


# n         2      3      4      5      6      7      8      9      10
A2 = [0,0, 1.880, 1.023, 0.729, 0.577, 0.483, 0.419, 0.373, 0.337, 0.308]
D3 = [0,0, 0,     0,     0,     0,     0,     0.076, 0.136, 0.184, 0.223]
D4 = [0,0, 3.267, 2.575, 2.282, 2.115, 2.004, 1.924, 1.864, 1.816, 1.777]
# n   0 1      2      3      4      5      6      7      8      9     10     11     12     13     14     15       20     25
c4 = [0,0,0.7979,0.8862,0.9213,0.9400,0.9515,0.9594,0.9650,0.9693,0.9727,0.9754,0.9776,0.9794,0.9810,0.9823]#,0.9869,0.9896]
B3 = [0,0,     0,     0,     0,     0, 0.030, 0.118, 0.185, 0.239, 0.284, 0.321, 0.354, 0.382, 0.406, 0.428]#, 0.510, 0.565]
B4 = [0,0, 3.267, 2.568, 2.266, 2.089, 1.970, 1.882, 1.815, 1.761, 1.716, 1.679, 1.646, 1.618, 1.594, 1.572]#, 1.490, 1.435]
B5 = [0,0,     0,     0,     0,     0, 0.029, 0.113, 0.179, 0.232, 0.276, 0.313, 0.346, 0.374, 0.399, 0.421]#, 0.504, 0.559]
B6 = [0,0, 2.606, 2.276, 2.088, 1.964, 1.874, 1.806, 1.751, 1.707, 1.669, 1.637, 1.610, 1.585, 1.563, 1.544]#, 1.470, 1.420]
A3 = [0,0, 2.659, 1.954, 1.628, 1.427, 1.287, 1.182, 1.099, 1.032, 0.975, 0.927, 0.886, 0.850, 0.817, 0.789]#, 0.680, 0.606]



def get_stats_x_mr_x(data, size):
    assert size == 1
    center = numpy.mean(data)
    sd = 0
    for i in range(len(data)-1):
        sd += abs(data[i] - data[i+1])
    sd /= len(data) - 1
    d2 = 1.128
    lcl = center - 3*sd/d2
    ucl = center + 3*sd/d2
    return center, lcl, ucl

def get_stats_x_mr_mr(data, size):
    assert size == 1
    sd = 0
    for i in range(len(data)-1):
        sd += abs(data[i] - data[i+1])
    sd /= len(data) - 1
    d2 = 1.128
    center = sd
    lcl = 0
    ucl = center + 3*sd/d2
    return center, lcl, ucl

def get_stats_x_bar_r_x(data, size):
    n = size
    assert n >= 2
    assert n <= 10

    Rsum = 0
    for xset in data:
        assert len(xset) == n
        Rsum += max(xset) - min(xset)
    Rbar = Rsum / len(data)

    Xbar = numpy.mean(data)

    center = Xbar
    lcl = center - A2[n]*Rbar
    ucl = center + A2[n]*Rbar
    return center, lcl, ucl

def get_stats_x_bar_r_r(data, size):
    n = size
    assert n >= 2
    assert n <= 10

    Rsum = 0
    for xset in data:
        assert len(xset) == n
        Rsum += max(xset) - min(xset)
    Rbar = Rsum / len(data)

    center = Rbar
    lcl = D3[n]*Rbar
    ucl = D4[n]*Rbar
    return center, lcl, ucl

def get_stats_x_bar_s_x(data, size):
    n = size
    assert n >= 2
    assert n <= 10

    Sbar = numpy.mean(numpy.std(data, 1, ddof=1))
    Xbar = numpy.mean(data)

    center = Xbar
    lcl = center - A3[n]*Sbar
    ucl = center + A3[n]*Sbar
    return center, lcl, ucl
    
def get_stats_x_bar_s_s(data, size):
    n = size
    assert n >= 2
    assert n <= 10

    Sbar = numpy.mean(numpy.std(data, 1, ddof=1))

    center = Sbar
    lcl = B3[n]*Sbar
    ucl = B4[n]*Sbar
    return center, lcl, ucl

def get_stats_p(data, size):
    n = size
    assert n > 1

    pbar = float(sum(data)) / (n * len(data))
    sd = numpy.sqrt(pbar*(1-pbar)/n)

    center = pbar
    lcl = center - 3*sd
    if lcl < 0:
        lcl = 0
    ucl = center + 3*sd
    if ucl > 1:
        ucl = 1.0
    return center, lcl, ucl

def get_stats_np(data, size):
    n = size
    assert n > 1

    pbar = float(sum(data)) / (n * len(data))
    sd = numpy.sqrt(n*pbar*(1-pbar))

    center = n*pbar
    lcl = center - 3*sd
    if lcl < 0:
        lcl = 0
    ucl = center + 3*sd
    if ucl > n:
        ucl = n
    return center, lcl, ucl

def get_stats_c(data, size):
    cbar = numpy.mean(data)

    center = cbar
    lcl = center - 3*numpy.sqrt(cbar)
    if lcl < 0:
        lcl = 0
    ucl = center + 3*numpy.sqrt(cbar)
    return center, lcl, ucl

def get_stats_u(data, size):
    n = size
    assert n > 1

    cbar = float(sum(data))/(len(data)*n)

    center = cbar
    lcl = center - 3*numpy.sqrt(cbar/n)
    if lcl < 0:
        lcl = 0
    ucl = center + 3*numpy.sqrt(cbar/n)
    return center, lcl, ucl

def prepare_data_none(data, size):
    return data

def prepare_data_x_bar_rs_x(data, size):
    data2 = []
    for xset in data:
        data2.append(numpy.mean(xset))
    return data2

def prepare_data_x_bar_r_r(data, size):
    data2 = []
    for xset in data:
        data2.append(max(xset) - min(xset))
    return data2

def prepare_data_x_bar_s_s(data, size):
    data2 = []
    for xset in data:
        data2.append(numpy.std(xset, ddof=1))
    return data2

def prepare_data_x_mr(data, size):
    data2 = [0]
    for i in range(len(data)-1):
        data2.append(abs(data[i] - data[i+1]))
    return data2

def prepare_data_p(data, size):
    data2 = [0]
    for d in data:
        data2.append(float(d)/size)
    return data2

def prepare_data_u(data, size):
    data2 = [0]
    for d in data:
        data2.append(float(d)/size)
    return data2

STATS_FUNCS = {
    CHART_X_BAR_R_X: (get_stats_x_bar_r_x, prepare_data_x_bar_rs_x),
    CHART_X_BAR_R_R: (get_stats_x_bar_r_r, prepare_data_x_bar_r_r),
    CHART_X_BAR_S_X: (get_stats_x_bar_s_x, prepare_data_x_bar_rs_x),
    CHART_X_BAR_S_S: (get_stats_x_bar_s_s, prepare_data_x_bar_s_s),
    CHART_X_MR_X: (get_stats_x_mr_x, prepare_data_none),
    CHART_X_MR_MR: (get_stats_x_mr_mr, prepare_data_x_mr),
    CHART_P: (get_stats_p, prepare_data_p),
    CHART_NP: (get_stats_np, prepare_data_none),
    CHART_C: (get_stats_c, prepare_data_none),
    CHART_U: (get_stats_u, prepare_data_u),
    CHART_EWMA: (None, prepare_data_none),
    CHART_CUSUM: (None, prepare_data_none),
    CHART_THREE_WAY: (None, prepare_data_none),
    CHART_TIME_SERIES: (None, prepare_data_none)}

RULES_FUNCS = {
    RULES_1_BEYOND_3SIGMA: (test_beyond_limits, 1),
    RULES_2_OF_3_BEYOND_2SIGMA: (None, 3),
    RULES_4_OF_5_BEYOND_1SIGMA: (None, 5),
    RULES_7_ON_ONE_SIDE: (test_violating_runs, 7),
    RULES_8_ON_ONE_SIDE: (test_violating_runs, 8),
    RULES_9_ON_ONE_SIDE: (test_violating_runs, 9),
    RULES_6_TRENDING: (None, 6),
    RULES_14_UP_DOWN: (None, 14),
    RULES_15_BELOW_1SIGMA: (None, 15),
    RULES_8_BEYOND_1SIGMA_BOTH_SIDES: (None, 8)}


class Spc_wxj(object):
    """
    Main class that provides SPC analysis. It detects SPC rules violations.
    It can draw charts using matplotlib.

    :arguments:
      data
       user data as flat array

    **Usage**

    >>> s = Spc([1, 2, 3, 3, 2, 1, 3, 8,1, 2, 3, 3, 2, 1, 3, 8,1, 2, 3, 3, 2, 1, 3, 8], CHART_X_MR_X)
    >>> s = Spc([1, 2, 3, 3, 2, 1, 3, 8,1, 2, 3, 3, 2, 1, 3, 8,1, 2, 3, 3, 2, 1, 3, 8], CHART_X_MR_MR)
    >>> s = Spc([[1, 2, 3],[1, 3, 8],[3, 2, 1],[3, 3, 8],[3, 3, 8],[3, 3, 3],[3, 4, 8],[5, 3,6],[8, 4, 8]], CHART_X_BAR_R_X)
    >>> s = Spc([[1, 2, 3],[1, 3, 8],[3, 2, 1],[3, 3, 8],[3, 3, 8],[3, 3, 3],[3, 4, 8],[5, 3,6],[8, 4, 8]], CHART_X_BAR_R_R)
    >>> s = Spc([[1, 2, 3],[1, 3, 8],[3, 2, 1],[3, 3, 8],[3, 3, 8],[3, 3, 3],[3, 4, 8],[5, 3,6],[8, 4, 8]], CHART_EWMA)
	
    >>> s = Spc([1, 2, 3, 3, 2, 1, 3, 8,1, 2, 3, 3, 2, 1, 3, 8,1, 2, 3, 3, 2, 1, 3, 8], CHART_EWMA)
    >>> s = Spc([1, 2, 3, 3, 2, 1, 3, 8,1, 2, 3, 3, 2, 1, 3, 8,1, 2, 3, 3, 2, 1, 3, 8], CHART_X_MR_X)
    >>> s = Spc([1, 2, 3, 3, 2, 1, 3, 8,1, 2, 3, 3, 2, 1, 3, 8,1, 2, 3, 3, 2, 1, 3, 8], CHART_X_MR_X)
    >>> s = Spc([1, 2, 3, 3, 2, 1, 3, 8,1, 2, 3, 3, 2, 1, 3, 8,1, 2, 3, 3, 2, 1, 3, 8], CHART_X_MR_X)
    >>> s.get_stats()
    (2.875, 1, 0.21542553191489322, 5.5345744680851068)
    >>> s.get_violating_points()
    {'1 beyond 3*sigma': [7]}
    """

    def __init__(self, data, chart_type, rules=RULES_BASIC, newdata=[], sizes=None):
        self.orig_data = data
        self.chart_type = chart_type
        self.rules = rules
        self.stats = []

        sf, pd = STATS_FUNCS[chart_type]
        if sizes == None:
            if isinstance(data[0], (list, tuple)):
                size = len(data[0])
            else:
                size = 1
        else:
            size = sizes
        self.center, self.lcl, self.ucl = sf(data, size)
        self._data = pd(data, size)

        self.violating_points = self._find_violating_points()

    def _find_violating_points(self, rules=[]):
        if len(rules) > 0:
            rs = rules
        else:
            rs = self.rules
        points = {}
        for i in range(len(self._data)):
            for r in rs:
                func, points_num = RULES_FUNCS[r]
                if func == None or i <= points_num - 1:
                    continue
                if func(self._data[i-points_num+1:i+1], self.center, self.lcl, self.ucl):
                    points.setdefault(r, []).append(i)
        return points

    def get_chart(self, ax=None):
        """Generate chart using matplotlib."""
        if not mpl_present:
            raise Exception("matplotlib not installed")
        if ax == None:
            ax = pylab
        #ax.title(u'标题')
        ax.plot(self._data, "bo-")#画数据线线
        ax.plot([0, len(self._data)], [self.center, self.center], "k-") #画一条中心线
        ax.plot([0, len(self._data)], [self.lcl, self.lcl], "k:")#画LCL线
        ax.plot([0, len(self._data)], [self.ucl, self.ucl], "k:")#画UCL线


        """
        上述代码展示了两种不同的曲线样式：'r-o' 和 'g--'。字母 'r' 和 'g' 代表线条的颜色，后面的符号代表线和点标记的类型。
        例如 '-o' 代表包含实心点标记的实线，'--' 代表虚线。其他的参数需要读者自己去尝试，这也是学习 Matplotlib 最好的方式。
        
        颜色： 蓝色 - 'b' 绿色 - 'g' 红色 - 'r' 青色 - 'c' 品红 - 'm' 黄色 - 'y' 黑色 - 'k'
        （'b'代表蓝色，所以这里用黑色的最后一个字母） 白色 - 'w' 
        线： 直线 - '-' 虚线 - '--' 点线 - ':' 点划线 - '-.' 
        常用点标记 点 - '.' 像素 - ',' 圆 - 'o' 方形 - 's' 三角形 - '^' 更多点标记样式点击https://matplotlib.org/api/markers_api.html
        """
        
        #对特殊的点标注颜色,这里可以用RULES进行优化函数
        if RULES_7_ON_ONE_SIDE in self.violating_points:           
            for i in self.violating_points[RULES_7_ON_ONE_SIDE]:
                ax.plot([i], [self._data[i]], "yo")
                
        if RULES_1_BEYOND_3SIGMA in self.violating_points:
            for i in self.violating_points[RULES_1_BEYOND_3SIGMA]:
                ax.plot([i], [self._data[i]], "ro")
                
        if RULES_8_ON_ONE_SIDE in self.violating_points:
            for i in self.violating_points[RULES_8_ON_ONE_SIDE]:
                ax.plot([i], [self._data[i]], "co")


        #return data
        #pylab.show()
        return self._data

    def get_violating_points(self, rules=[]):
        """Return points that violates rules of control chart"""
        return self.violating_points

    def get_stats(self):
        """Return basic statistics about data as tuple: (center, LCL, UCL)."""
        return self.center, self.lcl, self.ucl
    def get_data_mr(self):
        return self._data

    """
    **Usage**

    
    
    
    
    >>> s = Spc([[1, 2, 3],[1, 3, 8],[3, 2, 1],[3, 3, 8],[3, 3, 8],[3, 3, 3],[3, 4, 8],[5, 3,6],[8, 4, 8]], CHART_EWMA)
	
    >>> s = Spc([1, 2, 3, 3, 2, 1, 3, 8,1, 2, 3, 3, 2, 1, 3, 8,1, 2, 3, 3, 2, 1, 3, 8], CHART_EWMA)
    >>> s = Spc([1, 2, 3, 3, 2, 1, 3, 8,1, 2, 3, 3, 2, 1, 3, 8,1, 2, 3, 3, 2, 1, 3, 8], CHART_X_MR_X)
    >>> s = Spc([1, 2, 3, 3, 2, 1, 3, 8,1, 2, 3, 3, 2, 1, 3, 8,1, 2, 3, 3, 2, 1, 3, 8], CHART_X_MR_X)
    >>> s = Spc([1, 2, 3, 3, 2, 1, 3, 8,1, 2, 3, 3, 2, 1, 3, 8,1, 2, 3, 3, 2, 1, 3, 8], CHART_X_MR_X)
    >>> s.get_stats()
    (2.875, 1, 0.21542553191489322, 5.5345744680851068)
    >>> s.get_violating_points()
    {'1 beyond 3*sigma': [7]}
    

    CHART_X_BAR_R_X 均值控制图（极差）: >>> s = Spc([[1, 2, 3],[1, 3, 8],[3, 2, 1],[3, 3, 8],[3, 3, 8],[3, 3, 3],[3, 4, 8],[5, 3,6],[8, 4, 8]], CHART_X_BAR_R_X)
    CHART_X_BAR_R_R: 均值极差控制图 >>> s = Spc([[1, 2, 3],[1, 3, 8],[3, 2, 1],[3, 3, 8],[3, 3, 8],[3, 3, 3],[3, 4, 8],[5, 3,6],[8, 4, 8]], CHART_X_BAR_R_R)
    CHART_X_BAR_S_X: 均值控制图（标准差）>>> s = Spc([[1, 2, 3],[1, 3, 8],[3, 2, 1],[3, 3, 8],[3, 3, 8],[3, 3, 3],[3, 4, 8],[5, 3,6],[8, 4, 8]], CHART_X_BAR_S_X)
    CHART_X_BAR_S_S: 均值标准差控制图>>> s = Spc([[1, 2, 3],[1, 3, 8],[3, 2, 1],[3, 3, 8],[3, 3, 8],[3, 3, 3],[3, 4, 8],[5, 3,6],[8, 4, 8]], CHART_X_BAR_S_S)
    CHART_X_MR_X:单值控制图    >>> s = Spc([7.8,7.4,7.7,7,6.8,7.3,7.7,7.2,6.9,7.3,6.7,6.4,7.1,6.8,7,7.2,7.5,7.1,6.3,6.8,7.8,9,7.2,7.6,7.1,7.8], CHART_X_MR_X)
    CHART_X_MR_MR:单值极差控制图   >>> s = Spc([1, 2, 3, 3, 2, 1, 3, 8,1, 2, 3, 3, 2, 1, 3, 8,1, 2, 3, 3, 2, 1, 3, 8], CHART_X_MR_MR)
    CHART_P: (get_stats_p, prepare_data_p),
    CHART_NP: (get_stats_np, prepare_data_none),
    CHART_C: s = Spc([1, 2, 3, 3, 2, 1, 3, 8,1, 2, 3, 3, 2, 1, 3, 8,1, 2, 3, 3, 2, 1, 4,3, 8,9,10,11,12,24,17,23,25], CHART_C)

    CHART_U: (get_stats_u, prepare_data_u),
    CHART_EWMA: (None, prepare_data_none),
    CHART_CUSUM: (None, prepare_data_none),
    CHART_THREE_WAY: (None, prepare_data_none),
    CHART_TIME_SERIES: (None, prepare_data_none)}
    
    """
#s1 = Spc_wxj([6.64,6.64,6.65,6.63,6.65,6.65,6.64,6.63,6.62,6.61,6.64,6.64,6.62,6.64,6.61,6.62,6.63,6.64,6.63,6.64,6.63,6.64,6.65,6.63,6.63,6.51,6.52,6.51,6.54,6.52], CHART_X_MR_X)
#s2 = Spc_wxj([6.64,6.64,6.65,6.63,6.65,6.65,6.64,6.63,6.62,6.61,6.64,6.64,6.62,6.64,6.61,6.62,6.63,6.64,6.63,6.64,6.63,6.64,6.65,6.63,6.63,6.51,6.52,6.51,6.54,6.52], CHART_X_MR_MR)
#		"0":{"name":"1 beyond 3*sigma,一个点远离中心线超过3倍标准差","value":"[1,2],[2,6]"},
#		"1":{"name":"7 on one side，连续7个点在同一侧","value":"[1,2],[2,6]"}
