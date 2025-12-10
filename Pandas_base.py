#1. Pandasライブラリの読み込み
import pandas as pd

#2. 辞書を使ってデータフレームを作成する

date = {
    '商品名':['りんご', 'みかん', 'バナナ', 'ぶどう'],
    '価格': [150, 80, 100, 300],
    '在庫数': [10, 50, 25, 5]
}

# DateFrameの作成
df = pd.DataFrame(date)

#3. データフレーム全体を表示する
print("---1. データフレーム全体---")
print(df)

prices = df['価格']
print("\n---2. 価格の列だけ---")
print(prices)

#5.条件を指定して行を抽出する
expensive_items = df[df['価格'] >= 100]
print("\n---3. 100円以上の商品---")
print(expensive_items)