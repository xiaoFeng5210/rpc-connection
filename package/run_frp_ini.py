# 目前我们已经改好了文件，然后我们需要进入frp目录，开启一个线程，执行sudo ./frpc -c frpc.ini

import subprocess
import threading
import os

def run_frp_ini():
    # 指定 frp 目录的路径
    frp_dir = './frp'

    try:
        # 切换到 frp 目录
        os.chdir(frp_dir)

        print(f"当前工作目录: {os.getcwd()}")

        # 执行命令
        command = ['sudo', './frpc', '-c', 'frpc.ini']
        result = subprocess.run(command, check=True, capture_output=True, text=True)
        
        print("命令执行成功。输出：")
        print(result.stdout)

    except subprocess.CalledProcessError as e:
        print(f"命令执行失败。错误信息：")
        print(e.stderr)

    except FileNotFoundError:
        print(f"错误：找不到指定的目录或文件。请确保路径 '{frp_dir}' 正确，且 frpc 可执行文件存在。")

    except PermissionError:
        print("错误：权限不足。请确保您有足够的权限执行这个命令。")
    except Exception as e:
        print(f"发生未知错误：{e}")

    finally:
        # 切回原来的目录（可选，取决于您的需求）
        print("已经退出")

if __name__ == '__main__':
    thread = threading.Thread(target=run_frp_ini)
    thread.start()
    thread.join()
