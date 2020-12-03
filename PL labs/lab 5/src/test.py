import os

#Время последнего изменения файла
print(os.path.getmtime('C:/Users/Ivan/Desktop/Отчеты/PL labs/lab 5/src/filefunctions.py'))
#Время последнего доступа к файлу
print(os.path.getatime('C:/Users/Ivan/Desktop/Отчеты/PL labs/lab 5/src/filefunctions.py'))
#Размер файла в байтах
print(os.path.getsize('C:/Users/Ivan/Desktop/Отчеты/PL labs/lab 5/src/filefunctions.py'))
