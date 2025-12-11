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

#6. 新しい列を追加する (すべての行に同じ値を適用)
df['割引率'] = 0.1

#7. 既存の列を使って新しい列を計算する
#    (価格 * 在庫数) で在庫の合計金額を計算
df['合計金額'] = df['価格'] * df['在庫数']

#8. 新しいデータフレームの状態を確認
print("--- 4. 新しい列を追加・計算後 ---")
print(df)

#9. 平均値などの統計情報を計算する
average_price = df['価格'].mean() # ← mean() の丸括弧を忘れずに！
total_inventory = df['在庫数'].sum()

print(f"\n--- 5. 統計情報 ---")
print(f"平均価格: {average_price:.2f}円")
print(f"総在庫数: {total_inventory}個")