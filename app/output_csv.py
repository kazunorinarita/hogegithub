from datetime import datetime, date, time, timedelta
from .models import Item
import csv

t = date.today()
output_path = '/'
output_name = date.today() + t.strftime('%Y%m') + '_competency.csv'

# 検索対象レコードの抽出

order_list = Item.objects.all()

# CSV出力処理開始
with open(output_path + output_name, 'w', encoding='cp932', newline='') as csv_file:
    # 1行目にヘッダーを書き込む
    header = ['氏名', '自己評価', '一次評価', '二次評価']
    writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
    writer.writerow(header)

    for order in order_list:
        order_name = order.name
        order_self = order.flag
        order_primary = order.flag1
        order_secondary = order.flag2
        row = []
        row += [order_name, order_self, order_primary, order_secondary]

        writer.writerow(row)