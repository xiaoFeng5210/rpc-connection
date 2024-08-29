import typer
from config.password import device_match_password

def main_cli(device_name: str):
    if device_name in device_match_password:
        # typer.echo(f"Hello {device_name}, {device_match_password[device_name].get('password')}")
        find_obj = device_match_password[device_name]
        password = find_obj.get("password")
        desc = find_obj.get("desc")
        typer.echo(f"设备名称: {device_name}, 密码: {password}, 描述: {desc}")
        
    else:
        typer.echo(f"目前无法找到 {device_name}, ")  

if __name__ == "__main__":
    typer.run(main_cli)
