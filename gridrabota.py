#from tkinter import *
#root=Tk()

#Label(text="Имя:").grid(row=0, column=0)
#table_name = Entry(width=30)
#table_name.grid(row=0, column=1, columnspan=3)

#Label(text="Столбцов:").grid(row=1, column=0)
#table_column = Spinbox(width=7, from_=1, to=50)
#table_column.grid(row=1,column=1)
#Label(text="Строк:").grid(row=1, column=2)
#table_row=Spinbox(width=7, from_=1, to=100)
#table_row.grid(row=1, column=3)

#Button(text="Справка").grid(row=2, column=0)
#Button(text="Вставить").grid(row=2, column=2)
#Button(text="Отменить").grid(row=2, column=3)

#root.mainloop()


from tkinter import *
root=Tk()


root.title="Tunniplaan"
root.geometry("1200x900")
#Верхняя строка
Label(text="",font="Arial,60",width=10, height=5).grid(row=0, column=0)
Label(text="0",font="Arial,60",width=10).grid(row=0, column=1)
Label(text="1",font="Arial,60",width=10).grid(row=0, column=2)
Label(text="2",font="Arial,60",width=10).grid(row=0, column=3)
Label(text="3",font="Arial,60",width=10).grid(row=0, column=4)
Label(text="4",font="Arial,60",width=10).grid(row=0, column=5)
Label(text="5",font="Arial,60",width=10).grid(row=0, column=6)
Label(text="6",font="Arial,60",width=10).grid(row=0, column=7)
Label(text="7",font="Arial,60",width=10).grid(row=0, column=8)
Label(text="8",font="Arial,60",width=10).grid(row=0, column=9)
Label(text="9",font="Arial,60",width=10).grid(row=0, column=10)
Label(text="10",font="Arial,60",width=10).grid(row=0, column=11)
#Дни недели
Label(text="Esmaspäev",font="Arial,100",width=10,height=8).grid(row=1, rowspan=2, column=0)
Label(text="Teisipäev",font="Arial,100",width=10,height=8).grid(row=3, rowspan=2, column=0)
Label(text="Kolmapäev",font="Arial,100",width=10,height=8).grid(row=5, rowspan=2, column=0)
Label(text="Neljapäev",font="Arial,100",width=10,height=8).grid(row=7, rowspan=2, column=0)
Label(text="Reede",font="Arial,100",width=10,height=8).grid(row=9, rowspan=2, column=0)

#Esmaspäev
Label(text="Tugiõpe\n(eesti keel)",font="Arial,50",width=10,height=3,bg="pink",relief=RIDGE).grid(row=2, column=2)
Label(text="Logistikateenused",font="Arial,50",width=20,height=6,bg="green",relief=RIDGE).grid(row=1,rowspan=2, column=3,columnspan=2)
Label(text="Matemaatika",font="Arial,50",width=10,height=6,bg="red",relief=RIDGE).grid(row=1, rowspan=2, column=5)
Label(text="Matemaatika",font="Arial,50",width=10,height=6,bg="red",relief=RIDGE).grid(row=1, rowspan=2, column=6)
Label(text="Keel ja\nkirjandus",font="Arial,50",width=10,height=6,bg="lightgreen",relief=RIDGE).grid(row=1, rowspan=2, column=8)
Label(text="Keel ja\nkirjandus",font="Arial,50",width=10,height=6,bg="lightgreen",relief=RIDGE).grid(row=1, rowspan=2, column=9)
Label(text="Tugiõpe\n(matem)",font="Arial,50",width=10,height=6,bg="pink",relief=RIDGE).grid(row=1, rowspan=2, column=10)

#Teisipäev
Label(text="Tugiõpe\n(keemia)",font="Arial,50",width=10,height=6,bg="purple",relief=RIDGE).grid(row=3, rowspan=2, column=2)
Label(text="Programmeerimise\nalused",font="Arial,50",width=30,height=6,bg="lightblue",relief=RIDGE).grid(row=3, rowspan=2, column=3, columnspan=3)
Label(text="Füüsika",font="Arial,50",width=20,height=6,bg="pink",relief=RIDGE).grid(row=3, rowspan=2, column=7, columnspan=2)

#Kolmapäev
Label(text="Tugiõpe\n(eesti keel)",font="Arial,50",width=10,height=3,bg="pink",relief=RIDGE).grid(row=5, column=2)
Label(text="Kunstiained",font="Arial,50",width=20,height=6,bg="purple",relief=RIDGE).grid(row=5, rowspan=2, column=3,columnspan=2)
Label(text="Kehaline kasvatus",font="Arial,50",width=20,height=6,bg="purple",relief=RIDGE).grid(row=5, rowspan=2, column=6, columnspan=2)

#Neljapäev
Label(text="Logistikateenused",font="Arial,50",width=20,height=6,bg="green",relief=RIDGE).grid(row=7, rowspan=2, column=2, columnspan=2)
Label(text="Programmeerimise alused",font="Arial,50",width=20,height=6,bg="lightblue",relief=RIDGE).grid(row=7, rowspan=2, column=5, columnspan=2)
Label(text="Inglise keel",font="Arial,50",width=10,height=3,bg="yellow",relief=RIDGE).grid(row=7, column=7)
Label(text="Inglise keel",font="Arial,50",width=10,height=3,bg="yellow",relief=RIDGE).grid(row=7, column=8)
Label(text="Arenduskeskkonna\nloomine",font="Arial,50",width=20,height=3,bg="pink",relief=RIDGE).grid(row=8, column=7, columnspan=2)
Label(text="Arenduskeskkonna\nloomine",font="Arial,50",width=20,height=3,bg="pink",relief=RIDGE).grid(row=7, column=9, columnspan=2)
Label(text="Eesti keel",font="Arial,50",width=10,height=3,bg="grey",relief=RIDGE).grid(row=8, column=9)
Label(text="Eesti keel",font="Arial,50",width=10,height=3,bg="grey",relief=RIDGE).grid(row=8, column=10)
Label(text="Rühmajuhatajatund",font="Arial,50",width=10,height=6,bg="purple",relief=RIDGE).grid(row=7, rowspan=2, column=11)

#Reede
Label(text="Eesti keel",font="Arial,50",width=10,height=3,bg="purple",relief=RIDGE).grid(row=9, column=2)
Label(text="Eesti keel",font="Arial,50",width=10,height=3,bg="purple",relief=RIDGE).grid(row=9, column=3)
Label(text="Arenduskeskkonna\nloomine",font="Arial,50",width=20,height=3,bg="pink",relief=RIDGE).grid(row=10, column=2, columnspan=2)
Label(text="Programmeerimise alused",font="Arial,50",width=50,height=6,bg="lightblue",relief=RIDGE).grid(row=9, rowspan=2, column=4, columnspan=5)
Label(text="Arenduskeskkonna\nloomine",font="Arial,50",width=20,height=3,bg="pink",relief=RIDGE).grid(row=9,column=9, columnspan=2)
Label(text="Inglise keel",font="Arial,50",width=10,height=3,bg="yellow",relief=RIDGE).grid(row=10, column=9)
Label(text="Inglise keel",font="Arial,50",width=10,height=3,bg="yellow",relief=RIDGE).grid(row=10, column=10)

root=mainloop()