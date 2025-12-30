# Git 版本控制入門指南

版本控制系統 (Version Control System) 就像是程式碼的時光機。它可以幫您記錄每一次的修改，如果改壞了，隨時可以「回到過去」。Git 是目前世界上最流行的版本控制工具。

## 為什麼需要 Git?

1.  **備份**: 程式碼不再只存在您的電腦裡 (如果上傳到 GitHub)。
2.  **後悔藥**: 改錯了程式碼，可以輕鬆還原。
3.  **協作**: 多人一起開發同一個專案時，Git 能協助整合大家的程式碼。

## 基礎指令教學

請在 VS Code 的終端機 (Terminal) 中輸入以下指令。

### 1. 初始化 (Initialize)

如果是第一次開始使用 Git，需要先告訴 Git 這個資料夾要被管理。

```bash
git init
```

### 2. 檢查狀態 (Status)

隨時查看目前檔案的狀態 (哪些被修改了、哪些還沒被追蹤)。

```bash
git status
```

### 3. 加入追蹤 (Add)

告訴 Git 您想要記錄哪些檔案的變更。通常我們會加入所有檔案：

```bash
git add .
```
*注意：`.` 代表當前目錄下的所有檔案。*

### 4. 提交版本 (Commit)

將目前暫存的變更正式記錄下來，並附上一段說明文字 (Message)。

```bash
git commit -m "這是我的第一次提交"
```
*建議：訊息內容要清楚描述這次改了什麼，例如 "新增強柱弱梁計算功能" 或 "修正 CSV 讀取錯誤"。*

### 5. 查看紀錄 (Log)

查看過去的提交歷史。

```bash
git log
```
(按 `q` 可以離開檢視模式)

---

## 常見工作流程 (Workflow)

每次您完成一個小功能或修改一段程式碼後，建議執行以下步驟：

1.  `git status` (確認改了什麼)
2.  `git add .` (將變更加入暫存區)
3.  `git commit -m "完成 xxx 功能"` (存檔)

## 什麼是 .gitignore?

您可能會發現專案中有一個 `.gitignore` 檔案。這個檔案是用來告訴 Git **「不要」** 追蹤哪些檔案。
通常我們會忽略：
- 自動產生的暫存檔 (如 `__pycache__`)
- 虛擬環境資料夾 (如 `venv`)
- 敏感資料 (如密碼設定檔)

本專案已經為您準備好標準的 Python `.gitignore` 設定了。

## 進階：上傳到 GitHub

如果您想將程式碼備份到雲端 (GitHub)，請參考以下步驟 (需先註冊 GitHub 帳號)：

1. 在 GitHub 網站上新增一個 Repository (倉庫)。
2. 依照 GitHub 頁面上的提示，執行類似以下的指令：

```bash
git remote add origin https://github.com/您的帳號/您的專案名稱.git
git branch -M main
git push -u origin main
```

祝您版本控制順利！
