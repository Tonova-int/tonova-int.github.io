import pandas as pd
import datetime

# 讀取 CSV
df = pd.read_csv("products.csv")

# 生成 YML 檔案
with open("products.yml", "w", encoding="utf-8") as f:
    f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
    f.write('<!DOCTYPE yml_catalog SYSTEM "shops.dtd">\n')
    f.write(f'<yml_catalog date="{datetime.datetime.now().strftime("%Y-%m-%d %H:%M")}">\n')
    f.write('  <shop>\n')
    f.write('    <name>My Shop</name>\n')
    f.write('    <company>My Company</company>\n')
    f.write('    <url>https://myshop.com</url>\n')
    f.write('    <currencies>\n')
    f.write('      <currency id="USD" rate="1"/>\n')
    f.write('    </currencies>\n')
    f.write('    <categories>\n')
    f.write('      <category id="1">General</category>\n')
    f.write('    </categories>\n')
    f.write('    <offers>\n')

    for i, row in df.iterrows():
        f.write(f'      <offer id="{row["id"]}" available="true">\n')
        f.write(f'        <name>{row["title"]}</name>\n')
        f.write('        <price>0</price>\n')  # 沒有價格，先填 0
        f.write('        <currencyId>USD</currencyId>\n')
        f.write('        <categoryId>1</categoryId>\n')
        f.write('        <description>No description</description>\n')  # 沒有描述，填預設
        f.write('      </offer>\n')

    f.write('    </offers>\n')
    f.write('  </shop>\n')
    f.write('</yml_catalog>\n')
