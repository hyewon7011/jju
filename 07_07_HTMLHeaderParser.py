import os
from langchain.text_splitter import HTMLHeaderTextSplitter

# 입력 파일과 출력 경로 설정
input_file = "C:/Users/dlsgn/Desktop/방학/구혜원.html"  # HTML 파일 경로
output_dir = "SUB/RESULT"  # 결과 저장 디렉토리
output_file = os.path.join(output_dir, "HTMLHEADERTEXTSPLITTER_RESULT.TXT")  # 결과 파일 이름

# HTML 헤더 분할 기준 설정
headers_to_split_on = [
    ("h1", "Header 1"),
    ("h2", "Header 2"),
    ("h3", "Header 3"),
    ("h4", "Header 4"),
]

# HTMLHeaderTextSplitter 초기화
splitter = HTMLHeaderTextSplitter(headers_to_split_on=headers_to_split_on)

# HTML 파일 읽기 및 처리
try:
    # HTML 파일 읽기
    with open(input_file, "r", encoding="utf-8") as f:
        html_content = f.read()

    # 헤더 기준으로 분할
    split_results = splitter.split_text(html_content)

    # 결과 디렉토리 확인 및 생성
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 결과 저장
    with open(output_file, "w", encoding="utf-8") as f:
        for result in split_results:
            f.write(result + "\n")

    print(f"결과 파일이 생성되었습니다: {output_file}")

except FileNotFoundError:
    print(f"파일을 찾을 수 없습니다. 경로를 확인하세요: {input_file}")
except Exception as e:
    print(f"오류 발생: {e}")
