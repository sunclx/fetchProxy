import os
from sub_convert import sub_convert

#文件位置
input_source_file = './sub/literx'
output_file = './sub/literxClash.yml'

def write_file(file,content):
    file = open(output_file, 'w', encoding= 'utf-8')
    file.write(content)
    file.close()

if __name__ == '__main__':
    #转换
    input_source_file = os.path.abspath(input_source_file)  # 获取文件路径
    content = sub_convert.convert_remote(input_source_file,'clash')   #转换

    #写入
    
    
