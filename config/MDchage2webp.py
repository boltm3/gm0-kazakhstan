import os
import re

def replace_image_links(directory):
    # 定义一个正则表达式来匹配图片文件扩展名（用于提取文件名）
    image_extensions = re.compile(r'\.(jpg|jpeg|png|gif|bmp|tiff|webp|svg)\b', re.IGNORECASE)
    # 定义一个正则表达式来匹配 Markdown 中的图片路径
    image_links_pattern = re.compile(r'!\[.*?\]\((.*?)\)', re.IGNORECASE)

    # 检查目录是否存在
    if not os.path.exists(directory):
        print(f"目录 {directory} 不存在!")
        return

    # 遍历指定目录下的所有文件
    for root, dirs, files in os.walk(directory):
        for file in files:
            # 只处理 .md 文件
            if file.endswith('.md'):
                md_file_path = os.path.join(root, file)
                
                # 打开并读取 .md 文件
                try:
                    with open(md_file_path, 'r', encoding='utf-8') as md_file:
                        content = md_file.read()

                    # 查找文件内容中所有图片文件路径
                    image_links = image_links_pattern.findall(content)

                    # 替换图片链接
                    new_content = content
                    for link in image_links:
                        # 提取图片文件名
                        match = image_extensions.search(link)
                        if match:
                            # 仅使用文件名部分，并将扩展名替换为 .jpg
                            file_name = os.path.splitext(os.path.basename(link))[0] + '.jpg'
                            # 构造新的链接
                            new_link = f"https://[yours].webp.ee/{file_name}"
                            # 替换原始链接
                            new_content = new_content.replace(link, new_link)

                    # 如果内容有变化，保存新的文件
                    if new_content != content:
                        with open(md_file_path, 'w', encoding='utf-8') as md_file:
                            md_file.write(new_content)
                        print(f"已更新文件: {md_file_path}")
                
                except Exception as e:
                    print(f"无法读取文件 {md_file_path}，错误: {e}")

# 调用函数，传入 /en 目录
replace_image_links('C:/Users/[your user name]/Desktop/git/firstkz/boltm3learn/kz')  # 替换为你的实际路径
