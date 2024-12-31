from langchain_text_splitters import MarkdownHeaderTextSplitter

# Markdown 파일 경로 설정
markdown_file_path = "C:/Users/dlsgn/Desktop/방학/구혜원.md"  # 파일 경로를 원하는 파일로 수정하세요.

# Markdown 파일 읽기
with open(markdown_file_path, "r", encoding="utf-8") as file:
    markdown_document = file.read()

# 분할할 헤더 설정
headers_to_split_on = [
    ('#', 'Header 1'),
    ('##', 'Header 2'),
    ('###', 'Header 3'),
]

# MarkdownHeaderTextSplitter 초기화
markdown_splitter = MarkdownHeaderTextSplitter(
    headers_to_split_on=headers_to_split_on,
    strip_headers=True
)

# 헤더 기준으로 텍스트 분할
md_header_splits = markdown_splitter.split_text(markdown_document)

# 분할된 텍스트 출력
for header in md_header_splits:
    print(f"{header.page_content}")
    print(f"{header.metadata}", end="\n==============================\n")