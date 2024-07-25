import os
def testfile(drectory,suffix):
    for root,dirs,files in os.walk(drectory):
        for file in files:
            if file.endswith(suffix):
                print(os.path.join(root,file))




    # def contains_string_in_large_file(file_path, search_string):
    #     with open(file_path, 'r') as file:
    #         for line in file:
    #             if search_string in line:
    #                 return True
    #     return False
    #
    # # 使用示例
    # file_path = 'large_example.txt'  # 大文件路径
    # search_string = 'text to search'  # 要搜索的字符串
    #
    # if contains_string_in_large_file(file_path, search_string):
    #     print(f"'{search_string}' found in the file.")
    # else:
    #     print(f"'{search_string}' not found in the file.")