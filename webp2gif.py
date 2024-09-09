from PIL import Image
import os


def convert(file, output=""):
    filepath = str(file)
    output_path = str(output)

    # 如果没有指定输出路径，默认将 .webp 转换为 .gif，保存在相同位置
    if output_path == "":
        output_path = filepath[:-5] + ".gif"

    image = Image.open(filepath)
    image.info.pop('background', None)  # 删除背景信息
    image.save(output_path, 'gif', save_all=True)

    print(f"Success: {filepath} -> {output_path}")


def convert_all_webp_in_directory():
    # 获取当前脚本所在的目录
    current_directory = os.path.dirname(os.path.realpath(__file__))

    # 获取目录下所有文件
    all_files = os.listdir(current_directory)

    # 过滤出 .webp 文件
    webp_files = [f for f in all_files if f.endswith(".webp")]

    if not webp_files:
        print("No .webp files found in the current directory.")
        return

    # 逐个转换 .webp 文件为 .gif
    for webp_file in webp_files:
        webp_path = os.path.join(current_directory, webp_file)
        convert(webp_path)  # 调用转换函数，不指定输出路径，默认在同目录下生成 .gif 文件


if __name__ == "__main__":
    print("Converting all .webp files in the current directory to .gif...\n")
    convert_all_webp_in_directory()
