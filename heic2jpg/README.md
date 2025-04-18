# HEIC图片转换器

这是一个简单的HEIC图片转换工具，可以将HEIC格式的图片转换为JPG格式。

## 使用方法

### 命令行方式

1. 基本用法（输出目录默认为输入目录下的out文件夹）：

```bash
HEIC转换器.exe -i 输入目录路径
```

2. 指定输出目录：

```bash
HEIC转换器.exe -i 输入目录路径 -o 输出目录路径
```

### 参数说明

- `-i` 或 `--input`：必需参数，指定包含HEIC文件的输入目录路径
- `-o` 或 `--output`：可选参数，指定输出目录路径（默认为输入目录下的out文件夹）

## 注意事项

1. 确保输入目录中包含HEIC格式的图片文件
2. 如果输出目录不存在，程序会自动创建
3. 转换后的图片将保持原文件名，仅扩展名改为.jpg
4. 转换质量设置为95，以保证图片质量

## 依赖项

- Python 3.6+
- Pillow
- pillow-heif
