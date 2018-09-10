# -*- coding: utf-8 -*-
import random

# 用y = Θ1*x1 + Θ2*x2来拟合下面的输入和输出
# input1  1   2   5   4
# input2  4   5   1   2
# output  19  26  19  20
input_x = [[2104, 3], [1600, 3], [2400, 3], [1416, 2], [3000, 4]]  # 输入
y = [400, 330, 369, 232, 540]  # 输出
theta = [71.27, 0.1345, -8.738]  # θ参数初始化
loss = 10  # loss先定义一个数，为了进入循环迭代
step_size = 0.01  # 步长
eps = 0.0001  # 精度要求
max_iters = 10000  # 最大迭代次数
error = 0  # 损失值
iter_count = 0  # 当前迭代次数

err0 = [0, 0, 0, 0, 0]  # 求Θ0梯度的中间变量1
err1 = [0, 0, 0, 0, 0]  # 求Θ1梯度的中间变量2
err2 = [0, 0, 0, 0, 0]  # 求Θ2梯度的中间变量2

while (loss > eps and iter_count < max_iters):  # 迭代条件
    loss = 0
    err0sum = 0
    err1sum = 0
    err2sum = 0
    for i in range(5):  # 每次迭代所有的样本都进行训练
        pred_y = theta[0] + theta[1] * input_x[i][0] + theta[2] * input_x[i][1]  # 预测值
        print("pred_y", pred_y)
        err0[i] = (pred_y - y[i])
        err0sum = err0sum + err0[i]
        err1[i] = (pred_y - y[i]) * input_x[i][0]
        err1sum = err1sum + err1[i]
        err2[i] = (pred_y - y[i]) * input_x[i][1]
        err2sum = err2sum + err2[i]
    print("err0sum", err0sum)
    print("err1sum", err1sum)
    print("err2sum", err2sum)
    theta[0] = theta[0] - step_size * err0sum / 5  # 对应5式
    theta[1] = theta[1] - step_size * err1sum / 5  # 对应5式
    theta[2] = theta[2] - step_size * err2sum / 5  # 对应5式
    for i in range(5):
        pred_y = theta[0] + theta[1] * input_x[i][0] + theta[2] * input_x[i][1]  # 预测值
        error = (1 / (2 * 5)) * (pred_y - y[i]) ** 2  # 损失值
        loss = loss + error  # 总损失值
    iter_count += 1
    print("iters_count", iter_count)
    print ("loss", loss)
    print('theta: ', theta)
print('theta: ', theta)
print('final loss: ', loss)
print('iters: ', iter_count)