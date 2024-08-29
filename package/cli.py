import typer
from config.password import device_match_password
import os

def main_cli(device_name: str):
    if device_name in device_match_password:
        # typer.echo(f"Hello {device_name}, {device_match_password[device_name].get('password')}")
        find_obj = device_match_password[device_name]
        password = find_obj.get("password")
        desc = find_obj.get("desc")
        typer.echo(f"设备名称: {device_name}, 密码: {password}, 描述: {desc}")
        
        # 读文件修改文件
        # 获取当前脚本所在目录
        current_dir = os.path.dirname(os.path.abspath(__file__))
        frpc_path = os.path.join(current_dir, 'frp', 'frpc.ini')
        print(frpc_path)

    else:
        typer.echo(f"目前无法找到 {device_name}, ")  

if __name__ == "__main__":
    typer.run(main_cli)
