# 專案擴充指南：模組化設計練習

這份文件旨在引導您如何將「強柱弱梁檢核」專案擴充為一個功能更完整的應用程式。我們將重點放在**模組化 (Modularization)** 的概念上，這就像是將程式碼拆解成不同的樂高積木，每個積木負責單一的功能，最後再組裝起來。

## 核心概念：關注點分離 (Separation of Concerns)

在擴充功能之前，我們先規劃新的架構。為了避免所有程式碼都擠在 `main.py` 裡，我們將功能拆分為以下幾個模組：

1.  **資料輸入模組 (Importers)**: 負責讀取外部檔案 (.e2k, .xlsx)。
2.  **核心計算模組 (Calculator)**: 負責邏輯運算 (既有的 `scwb_calculator.py`)。
3.  **報告輸出模組 (Exporters)**: 負責產生報表 (.xlsx, .docx)。
4.  **使用者介面模組 (GUI)**: 負責與使用者互動，不處理計算。

---

## 練習 1: 資料輸入模組 (Importers)

**目標**: 支援從 ETABS 模型檔 (.e2k) 與 Excel 鋼筋表讀取資料。

### 建議實作方式
建立一個新檔案 `src/importers.py`。

```python
# src/importers.py

def parse_e2k_file(file_path):
    """
    讀取 .e2k 文字檔，解析出梁柱的幾何資訊與編號。
    
    提示: 
    1. 使用 open() 讀取檔案。
    2. 利用字串處理 (split, find) 抓取關鍵字。
    """
    pass

def load_reinforcement_excel(file_path):
    """
    讀取 Excel 檔案，獲取鋼筋配置資訊。
    
    提示:
    1. 使用 pandas 的 read_excel() 功能。
    """
    pass
```

**思考點**: 這個模組只在乎「如何把檔案變成 Python 看得懂的資料 (如 Dictionary 或 DataFrame)」，它不需要知道這些資料後來被拿去做了什麼運算。

---

## 練習 2: 報告輸出模組 (Exporters)

**目標**: 將計算結果輸出為 Excel 表格與 Word 計算書。

### 建議實作方式
建立一個新檔案 `src/exporters.py`。

```python
# src/exporters.py

def export_to_excel(results_df, output_path):
    """
    將結果 DataFrame 存為 Excel 檔。
    
    提示:
    1. 使用 pandas 的 to_excel()。
    """
    pass

def generate_word_report(results_df, output_path):
    """
    產生包含文字說明與表格的 Word 報告。
    
    提示:
    1. 需要安裝 python-docx 套件。
    2. 建立 Document 物件，加入標題與表格。
    """
    pass
```

**思考點**: 這個模組只負責「排版與存檔」，它不應該包含任何強柱弱梁的檢核公式。

---

## 練習 3: 使用者介面 (GUI)

**目標**: 脫離黑底白字的終端機，建立視窗介面。

### 建議實作方式
建立一個新檔案 `src/gui.py` (或 `app_ui.py`)。建議使用 Python 內建的 `tkinter` 庫，它是最適合初學者的 GUI 框架。

```python
# src/gui.py
import tkinter as tk
from tkinter import filedialog
# 引入我們自己寫的模組
from src.scwb_calculator import SCWBCalculator
from src import importers, exporters

class SCWBApp:
    def __init__(self, root):
        self.root = root
        self.root.title("強柱弱梁檢核工具")
        
        # 建立按鈕：選擇 E2K 檔案
        # 建立按鈕：選擇 Excel 檔案
        # 建立按鈕：開始計算
        
    def on_calculate_click(self):
        # 這是 "控制器 (Controller)" 的角色
        # 1. 呼叫 importers 讀取資料
        # 2. 呼叫 SCWBCalculator 進行計算
        # 3. 呼叫 exporters 輸出結果
        # 4. 在視窗上顯示 "完成"
        pass
```

**思考點**: GUI 只是個「殼」，它負責接收使用者的點擊，然後指揮其他模組工作。

---

## 進階觀念：模組化設計原則

在設計模組時，有兩個黃金準則：

### 1. 高內聚 (High Cohesion)
**一個模組應該只專注做好一件事情。**
- ❌ **壞的設計**：一個 `utils.py` 裡面同時有「讀取檔案」、「計算地震力」、「發送 Email」的功能。
- ✅ **好的設計**：`importers.py` 只負責讀檔，`calculator.py` 只負責計算。

### 2. 低耦合 (Low Coupling)
**模組之間應該盡量減少依賴。**
- ❌ **壞的設計**：`calculator.py` 裡面直接寫死 `print("計算完成")` (這樣計算邏輯就依賴了終端機輸出)。
- ✅ **好的設計**：`calculator.py` 只回傳數據，由 `main.py` 或 `gui.py` 決定要 `print` 還是顯示在視窗上。

---

## 進階觀念：例外處理原則 (Exception Handling)

程式在執行時難免會遇到錯誤 (例如檔案找不到、格式錯誤)。良好的例外處理能讓程式不會直接「閃退」，而是優雅地告訴使用者發生了什麼事。

### 1. 捕捉特定的錯誤
不要只寫 `except:`，這樣會把所有錯誤都吃掉 (包含你寫錯程式碼的 Bug)。

```python
# ❌ 不推薦
try:
    df = pd.read_csv(path)
except:
    print("出錯了")

# ✅ 推薦
try:
    df = pd.read_csv(path)
except FileNotFoundError:
    print("找不到檔案，請確認路徑。")
except pd.errors.EmptyDataError:
    print("檔案是空的。")
except Exception as e:
    print(f"發生未預期的錯誤: {e}")
```

### 2. 在對的地方處理錯誤
- **底層模組 (如 `importers.py`)**: 遇到錯誤通常**往上拋出 (raise)**，或者回傳 `None`，因為它不知道該怎麼跟使用者溝通。
- **介面層 (如 `gui.py`)**: 負責**捕捉 (catch)** 錯誤，並彈出視窗警告使用者。

```python
# src/importers.py (底層)
def load_data(path):
    if not path.endswith('.csv'):
        raise ValueError("只支援 CSV 格式")
    # ...

# src/gui.py (介面層)
def on_button_click():
    try:
        data = importers.load_data(user_input_path)
    except ValueError as err:
        messagebox.showerror("錯誤", str(err))  # 彈出視窗
```

---

## 建議的檔案架構

完成擴充後，您的專案結構會變得更有組織：

```text
Wilson-SCWB/
├── main.py               # 程式入口 (啟動 GUI)
├── requirements.txt      # 新增 openpyxl, python-docx
├── README.md
├── data/
│   ├── model.e2k         # (新) 模型檔
│   └── rebar.xlsx        # (新) 鋼筋檔
└── src/
    ├── __init__.py
    ├── scwb_calculator.py # 核心邏輯 (不變)
    ├── importers.py       # (新) 輸入處理
    ├── exporters.py       # (新) 輸出處理
    └── gui.py             # (新) 視窗介面
```

## 下一步

1. 更新 `requirements.txt`，加入 `openpyxl` (讀寫 Excel) 和 `python-docx` (寫 Word)。
2. 挑選一個模組開始實作，建議從 `importers.py` 開始。
