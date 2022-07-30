import re
import os

shuru = ".mp4" #输入文件后缀名
shuchu = ".mp4" #输出文件后缀名

def guolv(datalist):
    return [val for val in datalist if re.search(shuru, val)]

input_file = "./" #输入路径，默认为当前路径，不建议修改，建议直接复制本文件到路径下
output_file = "./output/" #输出路径
ffmpeg_path = "ffmpeg -i " #ffmpeg如果在path下则不用填写完整路径，注意末尾空格
ffmpeg_options = " -ar 44100 "#转码参数，注意首位均有空格
f = os.listdir(input_file) #列出当前目录下所有文件

for i, n in enumerate(guolv(f)):
    print("正在转换" + n)
    fix_name = '"%s"' % (n) #修复文件名带空格，但是仅能在默认路径下工作
    # print(ffmpeg_path + fix_name + ffmpeg_options + output_file + fix_name)
    os.system(ffmpeg_path + fix_name + ffmpeg_options + output_file + str(i) + shuchu) #如修改默认路径则应当在此补全
    # os.system(ffmpeg_path + fix_name + ffmpeg_options + output_file + fix_name)
