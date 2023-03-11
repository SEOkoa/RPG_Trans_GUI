from bs4 import BeautifulSoup as bs
import langid
import requests
import time
import seaborn as sns
import pandas as pd

encodings = ['utf-8', 'euc-kr', 'cp949']
for encoding in encodings:
    try:
        with open('DB_Item.csv', 'r', encoding=encoding) as f:
            df = pd.read_csv(f)
        break
    except UnicodeDecodeError:
        continue

eztransWeb = 'http://127.0.0.1:5000/translate?text='

df = df.fillna("") #NaN 제거용
df_translated = pd.DataFrame(columns=['KOR_NAME'])
df_need_ts = pd.DataFrame(columns=['번역이 필요한 칼럼']) #번역이 필요한 컬럼명과 위치를 저장


column_amount = len(df.columns) # 처음 파일을 불러와서 컬럼의 갯수를 셈
lang_count = 0 # 일본어 단어/문장의 갯수를 셈
column_count = 1
ts_count = 1

print("===일본어 문장 갯수===")
#  컬럼
for i, row in df.iterrows():
    columns_check = df.columns[i]

    # 행의 언어를 분석하기 위한 반복문
    for j, row in df.iterrows():
        is_japanese = row[columns_check]

        # 문자열이 아니면 에러 생기니까 그냥 뛰어넘도록 하자
        if type(is_japanese) == float:
            continue

        #언어 분석
        detected = langid.classify(is_japanese)

        # 일본어가 인식되면 번역 대상으로 본다
        if "ja" in detected:
            lang_count = lang_count + 1

    print(columns_check, lang_count) # 컬럼명과 일본어 감지된 수 출력

    #일본어가 포함되어 있다면 번역 필요 목록에 추가
    if lang_count > 0 :
        df_need_ts.loc[column_count] = [columns_check]
        lang_count = 0

    column_count = column_count + 1

    #컬럼의 갯수만큼 진행되면 탈출
    if i == column_amount-1:
        break

print("\n\n===번역 대상 컬럼 정보===")
df_need_ts = df_need_ts.reset_index(drop = True) #인덱스를 재정렬함
print(df_need_ts)

print("\n\n===번역 시작===")
# 일본어가 포함되어 있었으면 번역을 돌린다

for ts_count in range(len(df_need_ts)): # ts_count를 0부터 df_need_ts의 열 갯수만큼 반복
    col_name = df_need_ts.loc[ts_count, '번역이 필요한 칼럼']
    japanese_sentences = df[col_name]  # Get the Japanese sentences from df

    print("====", col_name, "====")
    for j, japanese_sentence in enumerate(japanese_sentences):
        # Request translation from EZTrans Web API
        url = f'http://127.0.0.1:5000/translate?text={japanese_sentence}'
        response = requests.get(url)
        korean_sentence = response.text.strip()

        # Replace Japanese sentence with translated Korean sentence in df
        df.loc[j, col_name] = korean_sentence

        print(korean_sentence)

# Save translated df as a new csv file
df.to_csv('exe_test.csv', index=False)