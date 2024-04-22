# 3-tier-site

## 需求

執行前要先 `pip install -r requirements.txt` 下載所需套件

匯入 `database` 資料夾內的資料

## 使用

```
# 使用 flask 啟動服務
flask run
```

## 說明

`web/templates` 包含所有的前端模板

前端模板皆繼承自 `web/templates/master.html`

CSS 檔案位於 `web/static/styles.css`

與資料庫連接的程式碼為 `web/conn.py`
