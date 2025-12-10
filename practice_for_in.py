# 処理対象のデータ（辞書を使用）
member_data = {
    "Aさん": 35,
    "Bさん": 12,
    "Cさん": 50,
    "Dさん": 8
}

#1. for文でデータ一つずつ確認しながら、特定の条件を判定する
print("参加資格チェック")
ADULT_AGE = 18

for name, age in member_data.items():

    if age >=ADULT_AGE:
        print(f"{name}({age}歳):参加資格あり (大人)")
    else:
        print(f"{name}({age}歳):参加資格なし (子供)")

# 2. 条件を満たす要素を数える
adult_count = 0
for age in member_data.values():

    if age >= ADULT_AGE:
        adult_count += 1

print(f"\n合計で、大人の参加資格を持つメンバーは{adult_count}人です。")
