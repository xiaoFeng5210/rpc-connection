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
    print(frpc_path)
    return frpc_path




def read_ini_to_json(file_path: str):
    config = configparser.ConfigParser()
    try:
        with open(file_path, 'r') as ini_file:
            config.read_file(ini_file)

            
    except FileNotFoundError:
        print(f"错误：文件 '{file_path}' 不存在。")
    except configparser.Error as e:
        print(f"解析配置文件时出错：{e}")
    except json.JSONDecodeError as e:
        print(f"转换 JSON 时出错：{e}")
    except Exception as e:
        print(f"发生未知错误：{e}")    
