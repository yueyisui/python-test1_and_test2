from tkinter import *
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

class MY_GUI():
    def __init__(self,init_window_name):
        self.init_window_name = init_window_name
        self.formula = ""
        self.result = 0
        
    def cal(self,str_temp):
        #计算公式
        self.formula += str_temp
        self.data_Text.insert(END, str_temp)
        if str_temp == "*":
            speaker.Speak("乘以") #语言播报
        elif str_temp == "-":
            speaker.Speak("减") #语言播报
        elif str_temp == ".":
            speaker.Speak("点") #语言播报
        elif str_temp == "/":
            speaker.Speak("除以") #语言播报
        elif str_temp == "(":
            speaker.Speak("括号") #语言播报
        elif str_temp == ")":
            speaker.Speak("括号") #语言播报
        else:
            speaker.Speak(str_temp) #语言播报
            
        
    def get_result(self):
        #计算结果
        try:
            self.result = eval(self.formula)
            self.result_Text.insert(END, self.result)
            if self.result>= 0: 
                speaker.Speak(f"等于{self.result}")
            else:
                speaker.Speak(f"等于负{abs(self.result)}")
            
        except ZeroDivisionError:
            print("除数不能为0") 
            speaker.Speak("不可以除以0") #语言播报
        self.formula = ""
        self.result = 0

        
    def clear_all(self):
        #清除所有变量
        self.data_Text.delete(0.0,END)
        self.result_Text.delete(0.0,END)
        speaker.Speak("清除")
        
    #设置窗口
    def set_init_window(self):
        self.init_window_name.title("小岳同学的计算器1.0")      #窗口名
        #500x300为窗口大小，+10 +10 定义窗口弹出时的默认展示位置                      
        self.init_window_name.geometry('500x300+500+250')
        #self.init_window_name["bg"] = "black"         #窗口背景色
        #self.init_window_name.attributes("-alpha",0.9)    #虚化，值越小虚化程度越高
        #标签
        self.label1 = Label(self.init_window_name, text="计算过程：")
        self.label1.grid(row=0, column=0)
        self.label2 = Label(self.init_window_name, text="计算结果：")
        self.label2.grid(row=0, column=4)
         #文本框
        self.data_Text = Text(self.init_window_name, width=33, height=3)  #原始数据录入框
        self.data_Text.grid(row=1, column=0, rowspan=1, columnspan=3)
        self.result_Text = Text(self.init_window_name, width=33, height=3)  #原始数据录入框
        self.result_Text.grid(row=1, column=3, rowspan=1, columnspan=3)     
        #按钮
        self.button0 = Button(self.init_window_name, text="0", bg="lightblue", width=33,command=lambda:self.cal("0"))  # 调用内部方法  加()为直接调用
        self.button0.grid(row=2, column=0, rowspan=1, columnspan=3)
        self.button1 = Button(self.init_window_name, text="1", bg="lightblue", width=10,command=lambda:self.cal("1"))  # 调用内部方法  加()为直接调用
        self.button1.grid(row=3, column=0)
        self.button2 = Button(self.init_window_name, text="2", bg="lightblue", width=10,command=lambda:self.cal("2"))  # 调用内部方法  加()为直接调用
        self.button2.grid(row=3, column=1)
        self.button3 = Button(self.init_window_name, text="3", bg="lightblue", width=10,command=lambda:self.cal("3"))  # 调用内部方法  加()为直接调用
        self.button3.grid(row=3, column=2)
        self.button4 = Button(self.init_window_name, text="4", bg="lightblue", width=10,command=lambda:self.cal("4"))  # 调用内部方法  加()为直接调用
        self.button4.grid(row=4, column=0)
        self.button5 = Button(self.init_window_name, text="5", bg="lightblue", width=10,command=lambda:self.cal("5"))  # 调用内部方法  加()为直接调用
        self.button5.grid(row=4, column=1)
        self.button6 = Button(self.init_window_name, text="6", bg="lightblue", width=10,command=lambda:self.cal("6"))  # 调用内部方法  加()为直接调用
        self.button6.grid(row=4, column=2)
        self.button7 = Button(self.init_window_name, text="7", bg="lightblue", width=10,command=lambda:self.cal("7"))  # 调用内部方法  加()为直接调用
        self.button7.grid(row=5, column=0)
        self.button8 = Button(self.init_window_name, text="8", bg="lightblue", width=10,command=lambda:self.cal("8"))  # 调用内部方法  加()为直接调用
        self.button8.grid(row=5, column=1)
        self.button9 = Button(self.init_window_name, text="9", bg="lightblue", width=10,command=lambda:self.cal("9"))  # 调用内部方法  加()为直接调用
        self.button9.grid(row=5, column=2)
        self.button10 = Button(self.init_window_name, text="+", bg="lightblue", width=10,command=lambda:self.cal("+"))  # 调用内部方法  加()为直接调用
        self.button10.grid(row=6, column=0)
        self.button11 = Button(self.init_window_name, text="—", bg="lightblue", width=10,command=lambda:self.cal("-"))  # 调用内部方法  加()为直接调用
        self.button11.grid(row=6, column=1)
        self.button12 = Button(self.init_window_name, text="X", bg="lightblue", width=10,command=lambda:self.cal("*"))  # 调用内部方法  加()为直接调用
        self.button12.grid(row=6, column=2)
        self.button15 = Button(self.init_window_name, text="/", bg="lightblue", width=10,command=lambda:self.cal("/"))  # 调用内部方法  加()为直接调用
        self.button15.grid(row=7, column=0)
        self.button14 = Button(self.init_window_name, text=".", bg="lightblue", width=10,command=lambda:self.cal("."))  # 调用内部方法  加()为直接调用
        self.button14.grid(row=7, column=1)
        self.button13 = Button(self.init_window_name, text="=", bg="lightblue", width=10,command=lambda:self.get_result())  # 调用内部方法  加()为直接调用
        self.button13.grid(row=7, column=2)
        self.button18 = Button(self.init_window_name, text="清除", bg="lightblue", width=33,command=lambda:self.clear_all())  # 调用内部方法  加()为直接调用
        self.button18.grid(row=7, column=3, rowspan=1, columnspan=3)
        
        self.button16 = Button(self.init_window_name, text="(", bg="lightblue", width=10,command=lambda:self.cal("("))  # 调用内部方法  加()为直接调用
        self.button16.grid(row=3, column=3)
        self.button17 = Button(self.init_window_name, text=")", bg="lightblue", width=10,command=lambda:self.cal(")"))  # 调用内部方法  加()为直接调用
        self.button17.grid(row=3, column=4)
    
def gui_start():
    init_window = Tk()              #实例化出一个父窗口
    my_window = MY_GUI(init_window)
    # 设置根窗口默认属性
    my_window.set_init_window()
    init_window.mainloop()          #父窗口进入事件循环，可以理解为保持窗口运行，否则界面不展示

gui_start() #d调用GUI