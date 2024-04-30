## IO 文件讀取

＄ file = open(file_name)：open() 函數返回一個文件對象,我們將其賦值給變量 file。

＄ file.read()：讀取整個文件的內容,並將其作為一個字符串返回。

＄ file.readline()：讀取文件的下一行,並返回該行的內容(包括換行符)。

＄ file.readlines()：讀取文件的所有行,並將它們作為一個列表返回。每個元素都是文件中的一行(包括換行符)。

＄ file.close():關閉文件

＄ file.seek(offset):移動文字讀取指標

```python
file = open("myfile.txt", encoding="utf-8")
print(file) # <_io.TextIOWrapper name='myfile.txt' mode='r' encoding='UTF-8'>
print(file.read())
file.seek(0)
print(file.read())
print(type(file.read())) # <class 'str'> -> 他會把東西轉成string
```

```python
# 讀文件
file.seek(0)
while True:
    line = file.readline()
    if line == "":break
    else:print(line)

file.close()
```

## encoding

| 編碼方式 | 特點                                                                                                                                                                       |
| -------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ASCII    | - 最早的字符編碼標準 <br>- 使用 7 位二進制數表示，後來擴展為 8 位，即標準的 ASCII 碼   <br>- 定義了 128 個字符，包括英文字母、數字、標點符號和控制字符                     |
| Unicode  | - 旨在涵蓋世界上所有的字符 <br>- 使用 16 位、32 位等不同位數的編碼 <br>- 目標是提供一個通用的字符編碼標準，以支援全球化                                                    |
| UTF-8    | - Unicode 的實現之一 <br>- 用於以字節編碼字符，支援全球字符 <br>- 使用變長編碼，根據字符的範圍使用不同數目的位元組 <br>- 兼容 ASCII，對於英文字母和符號，和 ASCII 編碼相同 |

## with statement & open file with modes

＄ use "with" make the code clear and readable

-   r = read
-   a = append
-   w = write（覆寫）
-   x = create

```python
with open("myfile.txt", mode="r") as my_file:
    all_content = my_file.read()
    print(all_content)
```

## os delete file & folder

```python
os.remove("delete.txt")
os.rmdir("deleteFolder") # 若資料夾內部不為空，會失敗
```

## Serialize & Deserialize

＄ 序列化（Serialize）：
將數據結構或對象轉換成特定格式，以便保存到文件、數據庫或傳輸。目的是將內存中的對象轉為可存儲或傳輸的格式，通常是字節流或文本。

＄ 反序列化（Deserialize）
將已序列化的數據或字節流轉換回原始的數據結構或對象。這使得我們可以從文件讀取序列化的數據，或接收網絡上的序列化數據，並將其還原為原始形式。

## pickle

＄ 對象保存與讀取： 將 Python 對象保存到文件，以便以後讀取使用。這對於保存和恢復應用程序的狀態、配置文件、緩存數據等非常有用。
＄ 進程間通信： 在多進程或多線程的應用中，pickle 可用於將對象在不同進程之間進行傳遞。

＄ 優點：

-   簡單易用。
-   支援多種對象類型： 可以序列化和反序列化幾乎所有的 Python 對象，包括自定義類別的實例、函數、模塊等。
-   擴展性： pickle 提供了對二進制協議的支援，使得存儲大型數據集時更高效。

＄ 缺點：

-   安全性

```python

import pickle

x = 10
y = 100
z = [1,2,3,4,5]
# 基礎寫法(不會這樣寫)
# 寫
with open("pickle_file","wb") as p_file:
    pickle.dump(x,p_file) # 寫進文件
    pickle.dump(y,p_file) # 寫進文件
    pickle.dump(z,p_file) # 寫進文件

# 讀
with open("pickle_file","rb") as p_file:
    print(pickle.load(p_file))
    print(pickle.load(p_file))
    print(pickle.load(p_file))


# 較常見的寫法
# 寫
def save_data():
    global x, y, z
    data = {"x":x, "y":y, "z":z}
    with open("pickle_file","wb") as p_file:
        pickle.dump(data, p_file)

save_data()

# 讀
x = None
y = None
z = None

def restore_data():
    global x, y, z
    with open("pickle_file","rb") as p_file:
        data = pickle.load(p_file)
        x = data["x"]
        y = data["y"]
        z = data["z"]

restore_data()
print(x,y,z)

```

## shelve

建立在 pickle 上（所以安全性也是低）。
在 puckle 裡面，open 會直接將該檔案放進來，若資料龐大，記憶體會被塞爆。

```python
# 寫文件
import shelve
int1 = [1,2,3,4,5]
int2 = [6,7,8,9,10]
int3 = [100,101,102,103]

with shelve.open("shelve_example", "c") as shelf:
    shelf["int1"] = int1
    shelf["int2"] = int2
    shelf["int3"] = int3


# 讀文件
with shelve.open("shelve_example", "r") as shelf:
    for key in shelf.keys(): print(key)
    print(shelf["int2"])

```

## LBYL vs EAFB

```python
# LBYL（預先判斷錯誤）
def save_devide1(x, y):
    if y==0:
        print("devide 0")
        return None
    else: return x/y
```

```python
# EAFB（先執行，在除錯）
def save_devide2(x, y):
    try:
        return x/y
    except ZeroDivisionError:
        print("devide 0")
        return None

```

## general syntax of exception handling

```python
try:
    # main codes
except exception_name1 as variable1:
    # exception handling here
except exception_name2 as variable2:
    # exception handling here
else:
    # will run if no exception
finally:
    # finally run on matter having exception or not

```

## 常見錯誤種類（common errors and exceptions）

## common errors and exceptions

-   SyntaxError（語法錯誤）：
    描述：程式碼的語法有錯誤，通常是拼寫錯誤、缺少冒號、錯誤的括號等。
-   IndentationError（縮進錯誤）：
    描述：程式碼的縮進不正確。
-   TypeError（類型錯誤）：
    描述：當一個操作或函數應用於不適當類型的對象時引發。
-   NameError（名稱錯誤）：
    描述：當試圖訪問未定義的變數或函數時引發。
-   ValueError（數值錯誤）：
    描述：當函數接收到的引數的類型正確但是值不合法時引發。
-   FileNotFoundError（文件不存在錯誤）：
    描述：當試圖打開一個不存在的文件時引發。
-   ZeroDivisionError（除以零錯誤）：
    描述：當試圖對數值進行除以零的操作時引發。
-   RecursionError（遞迴錯誤）：
    描述：當一個遞迴函數的層次過多，超出 Python 解釋器的遞迴限制時引發。默認情況下，Python 的遞迴限制是 3000 層，當超過這個限制時會引發 `RecursionError`。
-   KeyError（鍵錯誤）：
    描述：當試圖使用字典中不存在的鍵來存取值時引發。
-   IndexError（索引錯誤）：
    描述：當試圖使用不存在的索引訪問序列（例如列表、元組、字符串）的元素時引發。

## 自制 exception

```python
# 寫一個module.py，判斷奇偶數，輸入小於0抱錯
# one.py
# 繼承自 Python 內建的異常類別（RuntimeError）（還有像是ValueError 或 Exception）
class NegativeNumberException(RuntimeError):
    def __init__(self, age):
        super().__init__()
        self.age = age
        if self.age < 0:
            print("this is an invalid number.")

def enter_age(age):
    if age < 0:
        raise NegativeNumberException(age)
    if age % 2 == 0:
        print("this is an even age.")
    else:
        print("this is an odd age.")

# two.py
        import one

try:
    # one.enter_age(20)
    # one.enter_age(21)
    one.enter_age(-20)
except one.NegativeNumberException as error:
    print(error)

```

## Pylint（給建議用的）

＄ 安裝 > pip install pylint
＄ 執行偵錯 > % pylint ./one.py -r y

## OS 模組用法

＄ 獲取當前工作目錄

```python
import os

# 獲取當前工作目錄
current_directory = os.getcwd()
print("Current Directory:", current_directory)
# Current Directory: /path/to/your/current/working/directory
```

＄ 獲取當前目錄和上級目錄的符號表示

```python
# 當前目錄的表示方式
current_directory_symbol = os.curdir
print("Current Directory Symbol:", current_directory_symbol)

# 上一級目錄的表示方式
parent_directory_symbol = os.pardir
print("Parent Directory Symbol:", parent_directory_symbol)

# Current Directory Symbol: .
# Parent Directory Symbol: ..
```

＄ 列出當前目錄下的所有文件和文件夾

```python
# 獲取當前目錄下的所有文件和文件夾
all_files_and_folders = os.listdir()
print("All Files and Folders:", all_files_and_folders)
# All Files and Folders: ['file1.txt', 'file2.py', 'folder1', 'folder2']
```

＄ 路徑相關操作

```python
file_path = "/path/to/your/file.txt"

# 獲取文件路徑
directory = os.path.dirname(file_path)

# 獲取文件名
file_name = os.path.basename(file_path)

# 分離文件名和擴展名
base_name, extension = os.path.splitext(file_name)

print("Directory:", directory)
print("File Name:", file_name)
print("Base Name:", base_name)
print("Extension:", extension)
# Directory: /path/to/your
# File Name: file.txt
# Base Name: file
# Extension: .txt
```

＄ 目錄操作

```python
# 創建目錄
os.mkdir("new_directory")

# 遞歸創建目錄
os.makedirs("parent/child")

# 刪除空目錄
os.rmdir("new_directory")

# 遞歸刪除目錄
import shutil
shutil.rmtree("parent")
```

＄ 文件操作

```python
# 刪除文件
os.remove("file.txt")

# 重命名文件或目錄
os.rename("old_name.txt", "new_name.txt")
```

＄ 如果我們希望“delete files” 是放進垃圾桶，而不是直接刪除 -> use send2tuash module

```python
# 安裝module：pip install send2trash
import send2trash
send2trash.send2trash("<要刪除的檔案.txt>")
send2trash.send2trash("<要刪除的非空/空資料夾.txt>")

```

＄ 刪除飛空資料夾

```python
import shutil
shutil.rmtree("new_folder")
```
