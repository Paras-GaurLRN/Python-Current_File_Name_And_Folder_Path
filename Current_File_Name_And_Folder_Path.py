def Current_File_Name_And_Folder_Path() -> dict[str,str]:
    path_of_file : str = __file__
    name_of_file_list : list = path_of_file.split('\\')
    name_of_file : list = name_of_file_list[-1]
    path_of_folder : str  = '' 
    for index_of_element in range(len(name_of_file_list)-1):
        path_of_folder += name_of_file_list[index_of_element]+'\\'
    return {'Name':name_of_file,'Path Of Folder':path_of_folder}

'''
SHOWCASE
'''

print("PATH: ",Current_File_Name_And_Folder_Path()['Path Of Folder'])
print("NAME: ",Current_File_Name_And_Folder_Path()['Name'])