# 1.PyPDF
from langchain_community.document_loaders import PyPDFLoader

# 결과를 RESULT.TXT 파일에 기록
with open("RESULT.txt", 'a', encoding='utf-8') as output_file:  # 'a' 모드로 추가 기록

    # 1. PyPDFLoader 실행: PDF 텍스트 추출
    output_file.write("1. PyPDFLoader 실행: PDF 텍스트 추출\n")
    output_file.write("="*50 + "\n\n")  # 구분선 추가

    # 파일 경로 설정
    FILE_PATH = "C:/Users/dlsgn/Documents/GitHub/jju_2/(통합공고)_위메프·티몬·인터파크·AK몰·알렛츠_정산지연_피해_소상공인·중소기업에_대한_이커머스_플랫폼_입점_지원(일부변경).pdf"
    loader = PyPDFLoader(FILE_PATH)

    # PDF 로더 초기화
    docs = loader.load()

    # ## 문서의 내용 출력
    page_content = docs[0].page_content[:500]
    
    # 결과 기록
    output_file.write("## 문서의 내용 출력:\n")
    output_file.write(page_content)  # PDF 첫 번째 페이지 내용 출력
    output_file.write("\n\n")  # 공백 추가

    output_file.write("="*50 + "\n\n")  # 구분선 추가

print("PyPDFLoader 코드 실행 결과가 RESULT.txt 파일에 저장되었습니다.")


# 2.PyMuPDF
from langchain_community.document_loaders import PyMuPDFLoader

# 결과를 RESULT.TXT 파일에 기록
with open("RESULT.txt", 'a', encoding='utf-8') as output_file:  # 'a' 모드로 추가 기록

    # 2. PyMuPDFLoader 실행: PDF 텍스트 추출
    output_file.write("2. PyMuPDFLoader 실행: PDF 텍스트 추출\n")
    output_file.write("="*50 + "\n\n")  # 구분선 추가

    # 파일 경로 설정
    FILE_PATH = "C:/Users/dlsgn/Documents/GitHub/jju_2/(통합공고)_위메프·티몬·인터파크·AK몰·알렛츠_정산지연_피해_소상공인·중소기업에_대한_이커머스_플랫폼_입점_지원(일부변경).pdf"
    loader = PyMuPDFLoader(FILE_PATH)

    # 문서 로드
    docs = loader.load()

    # ## 문서의 내용 출력
    page_content = docs[0].page_content[:500]
    
    # 결과 기록
    output_file.write("## 문서의 내용 출력:\n")
    output_file.write(page_content)  # PDF 첫 번째 페이지 내용 출력
    output_file.write("\n\n")  # 공백 추가

    output_file.write("="*50 + "\n\n")  # 구분선 추가

print("PyMuPDFLoader 코드 실행 결과가 RESULT.txt 파일에 저장되었습니다.")


# 3.PyPDFium2
from langchain_community.document_loaders import PyPDFium2Loader

# 결과를 RESULT.TXT 파일에 기록
with open("RESULT.txt", 'a', encoding='utf-8') as output_file:  # 'a' 모드로 추가 기록

    # 3. PyPDFium2Loader 실행: PDF 텍스트 추출
    output_file.write("3. PyPDFium2Loader 실행: PDF 텍스트 추출\n")
    output_file.write("="*50 + "\n\n")  # 구분선 추가

    # 파일 경로 설정
    FILE_PATH = "C:/Users/dlsgn/Documents/GitHub/jju_2/(통합공고)_위메프·티몬·인터파크·AK몰·알렛츠_정산지연_피해_소상공인·중소기업에_대한_이커머스_플랫폼_입점_지원(일부변경).pdf"
    loader = PyPDFium2Loader(FILE_PATH)

    # 데이터 로드
    docs = loader.load()

    # ## 문서의 내용 출력
    page_content = docs[0].page_content[:500]
    
    # 결과 기록
    output_file.write("## 문서의 내용 출력:\n")
    output_file.write(page_content)  # PDF 첫 번째 페이지 내용 출력
    output_file.write("\n\n")  # 공백 추가

    output_file.write("="*50 + "\n\n")  # 구분선 추가

print("PyPDFium2Loader 코드 실행 결과가 RESULT.txt 파일에 저장되었습니다.")

# 4.PDFMiner
from langchain_community.document_loaders import PDFMinerLoader

# 결과를 RESULT.TXT 파일에 기록
with open("RESULT.txt", 'a', encoding='utf-8') as output_file:  # 'a' 모드로 추가 기록

    # 4. PDFMinerLoader 실행: PDF 텍스트 추출
    output_file.write("4. PDFMinerLoader 실행: PDF 텍스트 추출\n")
    output_file.write("="*50 + "\n\n")  # 구분선 추가

    # 파일 경로 설정
    FILE_PATH = "C:/Users/dlsgn/Documents/GitHub/jju_2/(통합공고)_위메프·티몬·인터파크·AK몰·알렛츠_정산지연_피해_소상공인·중소기업에_대한_이커머스_플랫폼_입점_지원(일부변경).pdf"
    loader = PDFMinerLoader(FILE_PATH)

    # 데이터 로드
    docs = loader.load()

    # ## 문서의 내용 출력
    page_content = docs[0].page_content[:500]
    
    # 결과 기록
    output_file.write("## 문서의 내용 출력:\n")
    output_file.write(page_content)  # PDF 첫 번째 페이지 내용 출력
    output_file.write("\n\n")  # 공백 추가

    output_file.write("="*50 + "\n\n")  # 구분선 추가

print("PDFMinerLoader 코드 실행 결과가 RESULT.txt 파일에 저장되었습니다.")


# 5.PDFPlumber
from langchain_community.document_loaders import PDFPlumberLoader

# 결과를 RESULT.TXT 파일에 기록
with open("RESULT.txt", 'a', encoding='utf-8') as output_file:  # 'a' 모드로 추가 기록

    # 5. PDFPlumberLoader 실행: PDF 텍스트 추출
    output_file.write("5. PDFPlumberLoader 실행: PDF 텍스트 추출\n")
    output_file.write("="*50 + "\n\n")  # 구분선 추가

    # 파일 경로 설정
    FILE_PATH = "C:/Users/dlsgn/Documents/GitHub/jju_2/(통합공고)_위메프·티몬·인터파크·AK몰·알렛츠_정산지연_피해_소상공인·중소기업에_대한_이커머스_플랫폼_입점_지원(일부변경).pdf"
    loader = PDFPlumberLoader(FILE_PATH)

    # 문서 로딩
    docs = loader.load()

    # ## 문서의 내용 출력
    page_content = docs[0].page_content[:500]
    
    # 결과 기록
    output_file.write("## 문서의 내용 출력:\n")
    output_file.write(page_content)  # PDF 첫 번째 페이지 내용 출력
    output_file.write("\n\n")  # 공백 추가

    output_file.write("="*50 + "\n\n")  # 구분선 추가

print("PDFPlumberLoader 코드 실행 결과가 RESULT.txt 파일에 저장되었습니다.")
