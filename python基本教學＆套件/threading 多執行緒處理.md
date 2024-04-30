## 同步與非同步

-   同步：「同一個步道」，只能依序排隊前進。
-   非同步：「不 ( 非 ) 同步道」，可以各走各的。

```python
"""沒有使用threading，會先執行aa()，結束後才是bb()"""
import time

def aa():
    i = 0
    while i<5:
        i = i + 1
        time.sleep(0.5)
        print('A:', i)

def bb():
    i = 0
    while i<50:
        i = i + 10
        time.sleep(0.5)
        print('B:', i)

aa()
bb()
```

```python
"""建立多執行緒"""
import threading
import time

def aa():
    i = 0
    while i<5:
        i = i + 1
        time.sleep(0.5)
        print('A:', i)

def bb():
    i = 0
    while i<50:
        i = i + 10
        time.sleep(0.5)
        print('B:', i)

a = threading.Thread(target=aa)  # 建立新的執行緒
b = threading.Thread(target=bb)  # 建立新的執行緒

a.start()  # 啟用執行緒
b.start()  # 啟用執行緒
```

## 建立 threading 基本方法

＄ `thread = threading.Thread(target=function, args)`

-   function 要在執行緒裡執行的函式
-   args 函式所需的引數，使用 tuple 格式，如果只有一個參數，格式 (參數,)

＄ 建立 threading 之後，就可以使用下列常用的方法：

-   start() 啟用執行緒。
-   join() 等待執行緒，直到該執行緒完成才會進行後續動作。
-   ident 取得該執行緒的標識符。
-   native_id 取得該執行緒的 id。
-   is_alive() 執行緒是否啟用，啟用 True，否則 False。

＄ 範例：

```python
"""
aa跟bb會開多執行緒完成後，才會執行cc
如果只加入 a.join() 而不加入 b.join()，則 cc() 會在 aa() 執行結束就開始。
"""
import threading
import time

def aa():
    i = 0
    while i<5:
        i = i + 1
        time.sleep(0.5)
        print('A:', i)

def bb():
    i = 0
    while i<50:
        i = i + 10
        time.sleep(0.5)
        print('B:', i)

def cc():
    i = 0
    while i<500:
        i = i + 100
        time.sleep(0.5)
        print('C:', i)

a = threading.Thread(target=aa)
b = threading.Thread(target=bb)
c = threading.Thread(target=cc)

a.start()
b.start()
a.join()   # 告訴主執行緒要等待 a 執行緒完成。換句話說，主執行緒會暫停執行，直到 a 執行緒結束。
b.join()   # 告訴主執行緒要等待 b 執行緒完成。換句話說，主執行緒會暫停執行，直到 b 執行緒結束。
c.start()  # 當 aa() 與 bb() 都完成後，才會開始執行 cc()
```

## Lock() 鎖定

＄ 當有全局變量，要給第一個執行緒處理完後，才給第二個執行緒。
＄ 範例：

```python
"""這樣寫的話，job1跟job2同時都在使用全局變量a,數字就會亂掉"""
import threading

def job1():
    global a
    for i in range(5):
        a+=1
        print("job1", a)

def job2():
    global a
    for i in range(5):
        a+=10
        print("job2", a)


a = 0
t1 = threading.Thread(target=job1)
t2 = threading.Thread(target=job2)
t1.start(),t2.start()
t1.join(), t2.join()

```

＄ 範例：

```python
"""使用lock"""
import threading

def job1():
    global a, lock
    lock.acquire() # 佔有資源
    for i in range(5):
        a+=1
        print("job1", a)
    lock.release() # 釋放

def job2():
    global a, lock
    lock.acquire() # 佔有資源
    for i in range(5):
        a+=10
        print("job2", a)
    lock.release() # 釋放

lock = threading.Lock()
a = 0
t1 = threading.Thread(target=job1)
t2 = threading.Thread(target=job2)
t1.start(),t2.start()
t1.join(), t2.join()

```

＄ 範例：
`python`
