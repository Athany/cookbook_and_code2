# 关于球的屏保 基于python的一个练习

import random
import tkinter


class RandomBall():
    '''
    定义运动的球的类
    '''

    def __init__(self, canvas, scrnwidth, scrnheight):
        '''
        canvas: 画布，所有的内容都应该在画布上呈现出来，此处通过此变量传入
        scrnwidth/scrnheigh:屏幕宽高
        '''
        self.canvas = canvas
        # 球出现的初始位置要随机，此处位置表示的球的圆心
        # xpos表示位置的x坐标
        self.xpos = random.randint(20, int(scrnwidth) - 20)
        self.ypos = random.randint(20, int(scrnheight) - 20)
        # ypos表示位置的y坐标

        # 定义球运动的速度
        # 模拟运动：不断的擦掉原来画，然后在一个新的地方再从新绘制
        # 此处xvelocity模拟x轴方向运动
        self.xvelocity = random.randint(4, 20)
        self.yvelocity = random.randint(4, 20)
        # 同理，yvelocity模拟的是y轴方向运动

        # 定义屏幕的大小
        self.scrnwidth = scrnwidth
        self.scrnheight = scrnheight
        # 定义屏幕的高度

        # 球的大小随机
        # 此处球的大小用半径表示
        self.radius = random.randint(20, 120)

        # 定义颜色
        # RGB表示法：三个数字，每个数字的值是0-255之间，表示红绿蓝三个颜色的大小
        # 在某些系统中，之间用英文单词表示也可以，比如red, green
        # 此处用lambda表达式
        c = lambda: random.randint(0, 255)
        self.color = '#%02x%02x%02x' % (c(), c(), c())

        # 以上函数代码忘了缩进了，自行处理

    def create_ball(self):
        '''
    用构造函数定义的变量值，在canvas上画一个球

# tkinter没有画圆形函数
# 只有一个画椭圆函数，画椭圆需要定义两个坐标，
# 在一个长方形内画椭圆，我们只需要定义长方形左上角和右下角就好
# 求两个坐标的方法是，已知圆心的坐标，则圆心坐标减去半径能求出
# 左上角坐标，加上半径能求出右下角坐标
'''
        x1 = self.xpos - self.radius
        y1 = self.xpos - self.radius
        x2 = self.xpos + self.radius
        y2 = self.xpos + self.radius

        # 继续球y1, x2, y2

        # 再有两个对角坐标的前提下，可以进行画圆
        # fill表示填充颜色
        # outline是外围边框颜色

        self.item = self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, outline=self.color)

    def move_ball(self):
        # 移动球的时候，需要控制球的方向
        # 每次移动后，球都有一个新的坐标
        self.xpos += self.xvelocity
        self.ypos += self.yvelocity
        # 同理计算ypos

        # 以下判断是会否撞墙
        # 撞了南墙就要回头
        # 注意撞墙的算法判断
        # 装到了右边墙
        if self.xpos + self.radius >= self.scrnwidth:
            self.xvelocity = -self.xvelocity
        if self.ypos + self.radius >= self.scrnheight:
            self.yvelocity = -self.yvelocity
        if self.xpos < self.radius:
            self.xvelocity = abs(self.xvelocity)
        if self.ypos < self.radius:
            self.yvelocity = abs(self.yvelocity)

        # 或者以下代码
        # self.xvelocity *= -1
        # 同理可以判断撞别的墙的算法

        # 在画布上挪动图画
        self.canvas.move(self.item, self.xvelocity, self.yvelocity)


class ScreenSaver():
    '''
    定义屏保的类
    可以被启动
    '''
    # 如何装随机产生的球？
    balls = list()

    def __init__(self):
        # 每次启动球的数量随机
        self.num_balls = random.randint(6, 20)

        self.root = tkinter.Tk()
        # 取消边框
        self.root.overrideredirect(1)

        # 任何鼠标移动都需要取消
        self.root.bind('<Motion>', self.myquit)
        # 同理，按动任何键盘都需要退出屏保

        # 得到屏幕大小规格
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()

        # w, h = self.root.winfo_screenwidth(), self.winfo_screenheight()

        # 创建画布，包括画布的归属，规格
        self.canvas = tkinter.Canvas(self.root, width=self.width, height=self.height)
        self.canvas.pack()

        # 在画布上画球
        for i in range(self.num_balls):
            ball = RandomBall(self.canvas, scrnwidth=self.width, scrnheight=self.height)
            ball.create_ball()
            self.balls.append(ball)

        self.run_screen_saver()
        self.root.mainloop()

    def run_screen_saver(self):
        for ball in self.balls:
            ball.move_ball()

        # after是200毫秒后启动一个函数，需要启动的函数是第二个参数
        self.canvas.after(20, self.run_screen_saver)

    def myquit(self, e):
        # 此处只是利用了事件处理机制
        # 实际上并不关心事件的类型

        self.root.destroy()


if __name__ == "__main__":
    # 启动屏保
    ScreenSaver()