import os , shutil
#------------------------------------------------------>




#------------------------------------------------------>
#To change the path

os.chdir(r'D:\Gui')
#------------------------------------------------------>

#I use it to check that the path is changed or not..
# path = os.getcwd()
# print(path)
# items = os.walk(r'D:\Gui')
# for current_path,folder_name,file_name in items:
#     print(f"Current_path: {current_path}")
#     print(f"folder_name: {folder_name}")
#     print(f"file_name: {file_name}")

#------------------------------------------------------>

#The project starts from here...
dict_extension = {
    'video_extension' : (".mp4, .mkv, .flv"),
    'audio_extension' : (".mp3,.ma4,.wav,.flac"),
    'doucment_extension' : (".doc, .pdf, .txt")
}

# folder1path = input("Enter the path of the folder: ")

# def file_finder(folder_path,file_extension):
#     new_file = []
#     for file in os.listdir(folder_path):
#         for extenstion in file_extension:
#             if file.endswith(extenstion):
#                 new_file.append(file)
#     return new_file
    

# print(file_finder(folder_path,doucment_extension))

# for extension_type, extension_tuple in dict_extension.items():
#     folder_name = extension_type.split('_')[0]+ 'Files'
#     folder_path = os.path.join(folder1path,folder_name)
#     os.mkdir(folder_path)
#     for i in (file_finder(folder1path,extension_tuple)):
#         path = os.path.join(folder1path,i)
#         new_path = os.path.join(folder_path,i)
#         shutil.move(path,new_path)







# print(file_finder(folder_path,extension_tuple))