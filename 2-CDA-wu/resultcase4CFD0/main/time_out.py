# coding:utf8
import time
import threading

 
def callback_func():
    strbuffer = 'MXairfoil: time out, call back.'
    print(strbuffer)
    raise Exception("MXairfoil: time out! zhaoba, shabidongxi huibuhui xiechengxu a caole")
 
 
def time_out(interval, callback=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            t =threading.Thread(target=func, args=args, kwargs=kwargs)
            t.setDaemon(True)  # 设置主线程技术子线程立刻结束
            t.start()
            t.join(interval)  # 主线程阻塞等待interval秒
            if t.is_alive() and callback:
                return threading.Timer(0, callback).start()  # 立即执行回调函数
                
            else:
                return
        return wrapper
    return decorator
 
 
@time_out(2, callback_func)
def task3(hh):
    print('**********task3****************')
    for i in range(3):
        time.sleep(1)
        print(i)
        print(hh)
 
 
@time_out(10, callback_func)
def task4(hh):
    from call_components import call_components
    print(hh)
    script_folder = 'C:/Users/y/Desktop/EnglishMulu/testCDA1'
    matlab_location = 'C:/Users/y/Desktop/MXairfoilCDA'
    shishi = call_components(script_folder,matlab_location)
    shishi.set_value(0.4,'tethk')
    shishi.call_matlab()
    shishi.call_IGG()
    shishi.call_Turbo()
    shishi.call_CFView()
 
 
if __name__ == '__main__':
    task3('参数')
    task4('MXairfoil: start test call outer exe.')