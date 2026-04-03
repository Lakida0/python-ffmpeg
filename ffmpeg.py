import os
import subprocess

ffmpeg_exec = "ffmpeg" #ffmpeg可执行文件路径
input_ext = ".flac" #输入文件后缀名
output_ext = ".wav" #输出文件后缀名
input_path = "./" #输入路径，默认为当前路径，不建议修改，建议直接复制本文件到路径下
output_path = "./output/" #输出路径
ffmpeg_options = "-ar 44100" #简单传统转码参数
ffmpeg_opt_list = ffmpeg_options.split() #将转码参数处理为列表。参数若有空格则使用下面一行
# ffmpeg_opt_list = ["-ar","44100","-metadata","title=My Title"] #若参数带空格请使用此行
files = [f for f in os.listdir(input_path)
         if os.path.isfile(os.path.join(input_path,f))
         and f.lower().endswith(input_ext)] #列出当前目录下所有文件
os.makedirs(output_path, exist_ok=True) #若文件夹不存在则直接创建

for i, filename in enumerate(files):
    print(f"正在转换：{filename}")
    base,ext = os.path.splitext(filename)
    out_name = base + output_ext
    ffmpeg_cmd = [ffmpeg_exec,"-i",filename,*ffmpeg_opt_list,os.path.join(output_path,out_name)] #使用原始文件名
    # ffmpeg_cmd = ["ffmpeg","-i",filename,*ffmpeg_opt_list,os.path.join(output_path,f"{i}{output_ext}")] #按序号生成文件名
    # print("执行命令："," ".join(ffmpeg_cmd)) #调试输出
    #实际执行
    try:
        subprocess.run(ffmpeg_cmd,check=True,text=True)
        print(f"成功转换：{out_name}")
    except subprocess.CalledProcessError:
        print(f"{filename} 转换失败，错误信息如上")
