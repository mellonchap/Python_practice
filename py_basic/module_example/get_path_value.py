import os, sys

#현재파일의 위치
print(os.path.abspath(__file__))

#현재 파일의 부모 디렉토리 path
print(os.path.abspath(os.path.dirname(__file__)))

print(sys.path)