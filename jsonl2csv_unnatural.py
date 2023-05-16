import json
import csv
from datetime import datetime

# 현재 시각을 문자열로 변환
current_time = datetime.now().strftime('%m-%d-%H%M')

# JSONL 파일 경로와 출력할 CSV 파일 경로를 지정하세요
input_file_path = 'core_data_100_KR.jsonl'
output_file_path = f'path_{current_time}.csv'

# JSONL 파일을 읽어들이는 함수
def read_jsonl_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            yield json.loads(line)

# JSONL 데이터를 CSV로 변환하는 함수
def convert_jsonl_to_csv(input_file_path, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['번호', 'instruction', 'constraints', 'output'])  # 헤더 작성

        for idx, item in enumerate(read_jsonl_file(input_file_path), start=1):
            instruction = item['instruction_with_input']
            constraints = item['constraints']
            output = item['output']
            csv_writer.writerow([idx, instruction, constraints, output])

# 변환 실행
convert_jsonl_to_csv(input_file_path, output_file_path)