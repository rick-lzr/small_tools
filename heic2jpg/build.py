import PyInstaller.__main__
import os

# 获取当前目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 设置图标路径（如果有的话）
# icon_path = os.path.join(current_dir, 'icon.ico')

# PyInstaller参数
params = [
    'converter.py',  # 主程序文件
    '--name=HEIC转换器',  # 生成的exe名称
    '--onefile',  # 打包成单个文件
    f'--icon=1.jpg',  # 设置图标（如果有的话）
    '--clean',  # 清理临时文件
    '--add-data=README.md;.',  # 添加说明文件
]

# 执行打包
PyInstaller.__main__.run(params) 