import threading
import time

def thread_body():
    t = threading.current_thread()
    for i in range(10):
        print('线程名称：%s, 第几次执行: %d' % (t.name, i+1))
        time.sleep(2)
    print('线程名称：%s, 执行完成' % (t.name))

t1 = threading.Thread(target=thread_body, name='线程1') # 创建线程对象
t2 = threading.Thread(target=thread_body, name='线程2') # 创建线程对象

t1.start() # 启动线程
t2.start() # 启动线程

t2 = threading.active_count()
print(t2) # 获取当前活动线程数 -> 1

t3 = threading.main_thread()
print(t3.name) # 获取主线程 -> MainThread