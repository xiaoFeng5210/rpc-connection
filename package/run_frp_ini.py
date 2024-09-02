# 目前我们已经改好了文件，然后我们需要进入frp目录，开启一个线程，执行sudo ./frpc -c frpc.ini

import subprocess
import threading

def run_frp_ini():
    try:
        result = subprocess.run(['sudo', '../frp', '-c', '../frp/frpc.ini'], check=True, capture_output=True, text=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"发生错误: {e.stderr}")

if __name__ == '__main__':
    thread = threading.Thread(target=run_frp_ini)
    thread.start()
    thread.join()
