import pandas as pd
import datetime

# 讀取 CSV
df = pd.read_csv("data/products.csv")

# 生成 YML 檔案
with open("data/products.yml", "w", encoding="utf-8") as f:
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
        f.write(f'      <offer id="{i+1}" available="true">\n')
        # 自動偵測欄位
        if "name" in df.columns:
            f.write(f'        <name>{row["name"]}</name>\n')
        if "price" in df.columns:
            f.write(f'        <price>{row["price"]}</price>\n')
            f.write('        <currencyId>USD</currencyId>\n')
        f.write('        <categoryId>1</categoryId>\n')
        if "description" in df.columns:
            f.write(f'        <description>{row["description"]}</description>\n')
        if "image_url" in df.columns and pd.notna(row["image_url"]):
            f.write(f'        <picture>{row["image_url"]}</picture>\n')
        f.write('      </offer>\n')

    f.write('    </offers>\n')
    f.write('  </shop>\n')
    f.write('</yml_catalog>\n')
