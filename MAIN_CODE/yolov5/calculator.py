from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
import tkinter.messagebox

class calculator():
    def __init__(self, image, value): # 레이어1[사진을 표시], 레이어2[버튼1[흑백변환], 버튼2[이미지 크기 변환]], 파일 불러오는 메뉴바
        self.window = Tk()
        self.window.title("calculator")
        self.window.geometry("1500x1500")
        self.window.resizable(False, False)
        simage = None
        self.value = value
        self.image = image

        #프레임 1 = 리사이즈, 흑백변환 기능 버튼 및 리사이즈할 숫자 입력 레이블
        frame1 = Frame(self.window,
                       width = 214,
                       height = 480,
                       relief = "solid")
        frame1.pack(side="left")

        #리사이즈 버튼 및 높이와 넓이 입력 레이블
        self.hentry = StringVar()
        self.hentry.set(self.value)

        #프레임 1 패킹
        self.h_entry.grid(row = 0,
                     column = 0)
        self.v_entry.grid(row = 1,
                     column = 0)

        frame2 = Frame(self.window,
                       relief = "ridge",
                       bd = 3)
        frame2.pack(side="right")

        self.imagelabel = Label(frame2,
                           width = 400,
                           height = 480,
                           image = self.image)
        self.imagelabel.image = self.image
        self.imagelabel.pack()

        self.window.mainloop()

    def close(self):
        self.quit()
        self.destroy()


