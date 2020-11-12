import os

def print_folder_info(path):
	if os.path.exists(path):
		
		folder_name = os.path.basename(os.path.dirname(path))
		print("Имя папки: " + str(folder_name))
		
		folder = os.listdir(path)
		print("Количество файлов в папке: " + str(len(folder)))

		for file_name in folder:
			print(file_name)
	else:
		print("Указан неверный путь")


path = input("Введите путь к папке: ")
print_folder_info(path)