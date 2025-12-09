#1. 辞書の定義
student_scores = {
    "Tanaka" : 85,
    "Sato" : 92,
    "Yamada" : 78
}

print(f"辞書の内容: {student_scores}")

#2. キーを使って値にアクセス
sato_score = student_scores["Sato"]
print(f"佐藤さんの点数: {sato_score}")

#3. 新しい要素の追加
student_scores["Suzuki"] = 65
print(f"要素追加後の辞書: {student_scores}")

#4.要素の値を更新
student_scores["Tanaka"] = 90
print(f"田中さんの点数を更新")

#5.辞書をfor文でループ処理 (キーだけ取り出す)
print("\n---全員の点数を表示---")
for name in student_scores:
    score = student_scores[name]
    print(f"{name}:{score}点")

