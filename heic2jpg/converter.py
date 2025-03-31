import os
import argparse
from pillow_heif import register_heif_opener
from PIL import Image

def convert_heic_to_jpg(input_dir, output_dir):
    """
    将指定目录下的所有HEIC文件转换为JPG格式
    
    Args:
        input_dir (str): 输入目录路径，包含HEIC文件
        output_dir (str): 输出目录路径，用于保存转换后的JPG文件
    """
    # 注册HEIF图像处理器
    register_heif_opener()
    
    # 确保输出目录存在
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 遍历输入目录中的所有文件
    for filename in os.listdir(input_dir):
        if filename.lower().endswith('.heic'):
            # 构建完整的输入文件路径
            input_path = os.path.join(input_dir, filename)
            
            # 构建输出文件路径（将.heic替换为.jpg）
            output_filename = os.path.splitext(filename)[0] + '.jpg'
            output_path = os.path.join(output_dir, output_filename)
            
            try:
                # 打开HEIC图像
                with Image.open(input_path) as img:
                    # 保存为JPG格式
                    img.save(output_path, 'JPEG', quality=95)
                print(f"成功转换: {filename} -> {output_filename}")
            except Exception as e:
                print(f"转换失败 {filename}: {str(e)}")

if __name__ == "__main__":
    # 创建命令行参数解析器
    parser = argparse.ArgumentParser(description='将HEIC文件转换为JPG格式')
    parser.add_argument('-i', '--input', required=True, help='输入目录路径，包含HEIC文件')
    parser.add_argument('-o', '--output', help='输出目录路径，用于保存转换后的JPG文件（默认为输入目录下的out文件夹）')
    
    # 解析命令行参数
    args = parser.parse_args()
    
    # 如果没有指定输出目录，使用默认路径（输入目录下的out文件夹）
    if not args.output:
        args.output = os.path.join(args.input, 'out')
    
    # 执行转换
    convert_heic_to_jpg(args.input, args.output)
