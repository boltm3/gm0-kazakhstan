import re

# 定义文件路径
input_file_path = r'C:\Users\dm\Desktop\1output_responses.txt'
output_file_path = r'C:\Users\dm\Desktop\extracted_content.txt'

# 定义函数来提取content并写入新文件
def extract_and_write_content(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as file:
        # 读取文件内容
        file_content = file.read()

    # 使用正则表达式提取content部分
    pattern = r"ChatCompletionOutputMessage\(role='assistant', content='(.*?)'\s*, tool_calls=\[\]\)"
    matches = re.findall(pattern, file_content, re.DOTALL)

    # 如果找到了匹配项，处理并写入新文件
    if matches:
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            for content in matches:
                # 按句子拆分
                sentences = content.split('\n')
                for sentence in sentences:
                    cleaned_sentence = sentence.strip()
                    if cleaned_sentence:  # 忽略空白句子
                        output_file.write(cleaned_sentence + '\n')
        print(f"提取的内容已写入到 {output_file_path}")
    else:
        print("没有找到匹配的内容。")

# 调用函数
extract_and_write_content(input_file_path, output_file_path)
