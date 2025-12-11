#Pandas_base.pyを持ってくる
import Pandas_base as pb

#Pandas_base.pyのデータフレームを定義する　
df = pb.create_inventory_df()

#データフレーム確認用
#print(df)

#在庫数が20個より多い商品の抽出
count = df[df['在庫数']>=20]
print(count)

#商品を10%値上げして、値上げ価格を新しい列に入れる
df['値上げ価格'] = df['価格']*1.1
print(df)

for row in df.itertuples():
    item_name = row.商品名
    item_price = row.価格
    print(f"商品名:{item_name},価格:{item_price}")