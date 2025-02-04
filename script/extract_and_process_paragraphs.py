from huggingface_hub import InferenceClient

# 创建Inferences客户端
client = InferenceClient(
    provider="together",
    api_key="hf_vhCZO...lwGkGe"
)

# 设置你想要添加的 prompt
prompt = "\n Please extract the key information from the information, delete unnecessary details, and keep the most important part. Then just make sure to write each key information into a separate sentence in order."

# 读取文件内容并分割成段落
file_path = r'C:\Users\dm\Desktop\modified_combined.md'
with open(file_path, 'r', encoding='utf-8') as file:
    content = file.read()

# 使用 '\n\n' 来分割内容
paragraphs = content.split('\n\n')

# 设置输出文件路径
output_file_path = r'C:\Users\dm\Desktop\output_responses.txt'

# 打开文件进行写入
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    # 遍历每个段落并发送给API
    for paragraph in paragraphs:
        # 在每个问题后附加 prompt
        full_question = paragraph + prompt
        
        messages = [
            {
                "role": "user",
                "content": full_question
            }
        ]

        # 请求API获取回复，使用新的模型 'deepseek-ai/DeepSeek-V3'
        completion = client.chat.completions.create(
            model="deepseek-ai/DeepSeek-V3", 
            messages=messages, 
            max_tokens=500
        )

        # 输出API的回答
        response = f"Question: {full_question}\nAnswer: {completion.choices[0].message}\n{'-'*50}\n"

        # 打印到控制台
        print(response)

        # 将输出写入文件
        output_file.write(response)

print(f"Responses saved to {output_file_path}")
