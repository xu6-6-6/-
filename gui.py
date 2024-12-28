import tkinter as tk
from tkinter import ttk
import random
import pyttsx3
import threading

class StudentRandomQuestionSystem:
    def __init__(self, master):
        self.master = master
        master.title("学生随机提问系统——by 徐琛沣")
        master.geometry("250x250")
        
        # 获取屏幕宽度和高度
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        
        # 设置窗口位置为右下角
        x = screen_width - 262
        y = screen_height - 282
        master.geometry(f"250x250+{x}+{y}")
        
        # 设置窗口始终置顶
        master.attributes("-topmost", True)
        
        self.label = None
        self.timer_label = None
        self.timer = None
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 350)  # 设置语速
        self.engine.setProperty('volume', 1.0)  # 设置音量
        self.engine.runAndWait()
        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        style.configure("TButton", font=("微软雅黑", 15), padding=5)
        style.configure("TLabel", font=("微软雅黑", 30))

        self.label = ttk.Label(self.master, text="", font=("微软雅黑", 40))
        self.label.pack(expand=True, pady=20)

        self.timer_label = ttk.Label(self.master, text="", font=("微软雅黑", 15), foreground="red")
        self.timer_label.pack(pady=10)

        self.random_button = ttk.Button(self.master, text="随机提问", style="TButton", command=self.display_random_student)
        self.random_button.pack(side=tk.BOTTOM, pady=20)

    def display_random_student(self):
        # 隐藏计时文字
        self.timer_label.pack_forget()
        self.master.update_idletasks()  # 刷新屏幕
        
        # 停止当前的语音播报
        self.engine.stop()
        
        # 取消当前计时器
        if self.timer:
            self.master.after_cancel(self.timer)
            self.timer = None
        
        # 选择新的随机名字
        students = ['李致远', '徐琛沣', '李佑安', '焦羽桐', '马嘉贤',
                    '高语泽', '付涛滔', '张鹏飞', '段怡宁', '李延慧',
                    '徐嘉庆', '唐文博', '宋诚恩', '杨万杰', '王韬喻', 
                    '时静涵', '娄梦涵', '邱子涵', '张闵翔', '冯甘霖',
                    '杨慧', '周博', '王陌', '杨彪', '李柄融', 
                    '蔡煜喆', '赵宁南', '李一宁', '袁柳源', '畅张亦',
                    '王政杰', '户俊杰', '窦熙贝', '张梓轩', '高诚潞',
                    '李佳潞', '田佳禾', '连涵星', '狄谦钰', '王佑源',
                    '祁勇皓', '张意钦', '海珺媛',

                    '李致远', '李佑安', '焦羽桐', '马嘉贤',
                    '高语泽', '付涛滔', '张鹏飞', '段怡宁', '李延慧',
                    '徐嘉庆', '唐文博', '宋诚恩', '杨万杰', '王韬喻', 
                    '时静涵', '娄梦涵', '邱子涵', '张闵翔', '冯甘霖',
                    '杨慧', '周博', '王陌', '杨彪', '李柄融', 
                    '蔡煜喆', '赵宁南', '李一宁', '袁柳源', '畅张亦',
                    '王政杰', '户俊杰', '窦熙贝', '张梓轩', '高诚潞',
                    '李佳潞', '田佳禾', '连涵星', '狄谦钰', '王佑源',
                    '祁勇皓', '张意钦', '海珺媛', ]
        selected_student = random.choice(students)
        self.label.config(text=selected_student)
        self.master.update_idletasks()  # 刷新屏幕
        
        # 进行新的语音播报并显示计时文字
        threading.Thread(target=self.speak_student_name, args=(selected_student,)).start()

    def speak_student_name(self, name):
        self.master.update_idletasks()  # 刷新屏幕
        self.engine.stop()  # 确保停止当前的语音播报
        self.engine.say(f"请 {name} 同学回答问题")
        self.engine.runAndWait()  # 开始语音播报并等待完成
        self.master.update_idletasks()  # 刷新屏幕
        self.timer_label.pack(pady=10)  # 显示计时文字
        self.master.update_idletasks()  # 刷新屏幕
        self.reset_timer()  # 在语音播报完成后开始计时

    def reset_timer(self):
        if self.timer:
            self.master.after_cancel(self.timer)
        self.timer_label.config(text="00:00")
        self.update_timer()

    def update_timer(self):
        current_time = self.timer_label.cget("text")
        minutes, seconds = map(int, current_time.split(":"))
        seconds += 1
        if seconds == 60:
            minutes += 1
            seconds = 0
        self.timer_label.config(text=f"{minutes:02}:{seconds:02}")
        self.timer = self.master.after(1000, self.update_timer)

if __name__ == "__main__":
    root = tk.Tk()
    app = StudentRandomQuestionSystem(root)
    root.mainloop()