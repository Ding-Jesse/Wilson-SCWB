# Strong Column Weak Beam (SCWB) Analysis Project

這是一個專為非軟體開發者設計的 Python 練習專案。本專案的目的是透過程式碼來自動化檢查鋼筋混凝土結構中的「強柱弱梁」設計原則。

## 專案背景

**強柱弱梁 (Strong Column Weak Beam)** 是耐震設計中的一個重要概念。它的目的是確保在強烈地震發生時，塑性鉸 (Plastic Hinge) 會先發生在梁上，而不是柱子上。因為柱子的破壞通常會導致結構瞬間崩塌，而梁的破壞則能吸收能量並爭取逃生時間。

一般檢核公式 (簡化版):
$$ \sum M_c \ge 1.2 \sum M_b $$

其中：
- $\sum M_c$: 接頭處柱子的彎矩強度總和
- $\sum M_b$: 接頭處梁的彎矩強度總和
- $1.2$: 安全係數 (依規範可能不同)

## 檔案結構

- `main.py`: 程式的執行入口。
- `src/`: 包含主要的計算邏輯程式碼。
  - `scwb_calculator.py`: 定義了計算強柱弱梁的類別與方法。
- `data/`: 存放輸入與輸出的資料。
  - `sample_data.csv`: 範例輸入資料。
  - `results.csv`: 程式執行後產生的結果。
- `requirements.txt`: 專案所需的 Python 套件列表。

## 如何開始

### 1. 安裝 Python

請確保您的電腦已安裝 Python (建議版本 3.8 以上)。

### 2. 安裝相依套件

在終端機 (Terminal) 中執行以下指令來安裝必要的套件：

```bash
pip install -r requirements.txt
```

### 3. 執行程式

在終端機中執行以下指令：

```bash
python main.py
```

程式執行後，您會在螢幕上看到計算結果，並且在 `data/` 資料夾中會產生一個 `results.csv` 檔案。

## 練習方向

1. **修改數據**: 試著修改 `data/sample_data.csv` 中的數值，看看結果有什麼變化。
2. **調整係數**: 在 `main.py` 中，嘗試修改 `SCWBCalculator(factor=1.2)` 的 `factor` 數值 (例如改為 1.4)，觀察對結果的影響。
3. **擴充功能**: 試著在 `src/scwb_calculator.py` 中加入更多的檢查邏輯，例如加入軸力的影響 (進階)。

## 常見問題

- **Q: 為什麼執行時出現 `ModuleNotFoundError`?**
  - A: 請確認您是否已執行 `pip install -r requirements.txt`。

- **Q: 如何開啟 CSV 檔案?**
  - A: 您可以使用 Excel 或任何文字編輯器開啟 CSV 檔案。

## 單元測試 (Unit Testing)

為了確保程式邏輯正確，我們可以使用 `pytest` 來進行自動化測試。

### 1. 安裝 pytest
如果您尚未安裝，請執行：
```bash
pip install pytest
```
(如果您已經執行過 `pip install -r requirements.txt`，則已經安裝好了)

### 2. 執行測試
在終端機中輸入以下指令：
```bash
pytest
```
程式會自動尋找 `tests/` 資料夾中的測試檔案並執行。如果看到綠色的 `PASSED`，代表測試通過！

## 版本控制 (Git)

本專案已配置 `.gitignore` 檔案，方便您使用 Git 進行版本控制。
如果您是第一次接觸 Git，請參考我們準備的入門指南：

👉 **請閱讀：[Git 版本控制入門指南 (docs/GIT_TUTORIAL.md)](docs/GIT_TUTORIAL.md)**

## 進階練習：模組化擴充

如果您已經熟悉基本的 Python 操作，歡迎挑戰將本專案擴充為完整的視窗應用程式！
我們為您準備了一份詳細的指引文件，教您如何加入以下功能：
1. 讀取 ETABS .e2k 模型檔
2. 讀取 Excel 鋼筋資料
3. 輸出 Word 計算書
4. 製作圖形化介面 (GUI)

👉 **請閱讀：[專案擴充指南 (docs/FEATURE_EXPANSION_GUIDE.md)](docs/FEATURE_EXPANSION_GUIDE.md)**

祝您學習愉快！
