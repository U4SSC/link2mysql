# link2mysql

## usage
1. 開一個資料庫，將upload資料夾中的csv檔匯入mysql
2. 建立一個檔案config.py，可以參考config_example.py(因為每個人的設定可能不同，因此放在.gitignore)
3. 下載flask，flask的使用教學可以到以下網址查看
   - https://ooooooooooooooooooooooo.ooo/ooooοооoοᴏοoοᴏοoοᴏooοᴏoᴏoᴏооoоᴏᴏoоᴏᴏοоοoοоοοοᴏοоοᴏoᴏoоᴏоοᴏοoοᴏοᴏoоᴏᴏοᴏooοоᴏᴏοᴏoᴏοᴏοooоᴏᴏoᴏοooᴏοooᴏоo
4. 下載python mysql套件PyMySQL，教學可以到以下網址查看
   - https://ooooooooooooooooooooooo.ooo/ooooοооoοᴏοoοᴏοoοᴏooοᴏoᴏoᴏооoоᴏᴏoоᴏᴏοᴏоοοоoοοоᴏоοᴏοᴏοоοοοооοoоᴏοοоᴏoοооοοᴏοοoоᴏоοоᴏοοоοοοоοoοооοοᴏοοοоᴏοoоᴏоοоoᴏοоᴏᴏοоᴏοoоᴏᴏοᴏooοᴏоοοᴏοoοооoοоᴏᴏοоᴏоoоοοοoοοoᴏоooоοοοooоoᴏoᴏoоοοoᴏоooᴏοᴏoоοοοoοοoᴏοоoоοοoᴏоοoᴏοоoоοοoᴏоοoᴏоοoоοοοoοοoᴏοοoоοοοooоοooοoоοοοooοοooоoоοοοoοοoᴏοοoоοοοooοοoοooоοοοooоoᴏоooоοοοoοοoᴏοᴏoоοοοooоοoοоoоοοoᴏоοoᴏoоoоοοοoοοoᴏοᴏoоοοοooοοoοooоοοoᴏоooᴏοоoоοοοoοοoᴏоooоοοοooοoᴏоooоοοoᴏоοoᴏоooоᴏοoоοοοoοοoᴏοοoоοοoᴏоοοooоoоοοoᴏоοοooоoоᴏοoоοοοoοοoᴏοooоοοοooоοoοooоοοοooоοoοоoоοοοoοοoᴏοᴏoоοοoᴏоοoᴏοooоοοοooοoᴏоoοᴏooοᴏоοοоᴏοοᴏоοοᴏoᴏοᴏoοοоᴏooоοοοoοοoᴏοоoоοοοooοoᴏоooоοοοooοoᴏoοoоοοοoοοoᴏοᴏoоοοοooоoᴏοοoоοοoᴏоooᴏοooоᴏοoᴏοᴏoᴏоοοоoᴏoᴏоοoᴏоοoᴏοooᴏoοoᴏoooᴏоooᴏоoοоοooᴏoо
5. 執行python app.py就可以了~ 該怎麼進入網頁就點執行後出現的那個網址
6. 然後有個KPI_1，點進去可以看到將資料表內容全部印出的結果

## dbconnect's usage
```python
import dbconnect
data = dbconnect.select_all("kpi_1") # 其中kpi_1為資料表名稱，data裡面會得到那個資料表的全部資料，需要再做其他處理
```
