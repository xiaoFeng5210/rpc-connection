import os
import json
import configparser


def create_file_path():
    # 读文件修改文件
    # 获取当前脚本所在目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # 获取上层目录
    parent_dir = os.path.dirname(current_dir)
    frpc_path = os.path.join(parent_dir, 'frp', 'frpc.ini')
    return frpc_path




def modify_frp_ini(file_path: str, new_server_name: str):
    config = configparser.ConfigParser()
    try:
        with open(file_path, 'r') as ini_file:
            config.read_file(ini_file)
            if 'secret_ssh_visitor' in config:
                config['secret_ssh_visitor']['server_name'] = 'ssh_' + new_server_name
            else:
                print("警告: 'secret_ssh_visitor' 部分不存在")

            with open(file_path, 'w') as ini_file:
                config.write(ini_file)
                print(f"成功修改 '{file_path}'文件")

    except FileNotFoundError:
        print(f"错误：文件 '{file_path}' 不存在。")
    except configparser.Error as e:
        print(f"解析配置文件时出错：{e}")
    except json.JSONDecodeError as e:
        print(f"转换 JSON 时出错：{e}")
    except Exception as e:
        print(f"发生未知错误：{e}")

def create_frp_ini(device_name: str):
    file_path = create_file_path()
    modify_frp_ini(file_path, device_name)

if __name__ == "__main__":
    create_frp_ini('nothing') 
