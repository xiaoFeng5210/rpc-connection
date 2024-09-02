import typer
from config.password import device_match_password
from package.file import create_frp_ini
from package.run_frp_ini import run_frp_ini

current_device = ''
current_password = ''

def main_cli(device_name: str):
    # 检查设备名称是否在设备匹配密码字典中
    if device_name in device_match_password:
        # 如果设备名称在字典中，则获取密码和描述信息
        find_obj = device_match_password[device_name]
        find_obj = device_match_password[device_name]
        password = find_obj.get("password")
        desc = find_obj.get("desc")
        if password is not None:
            typer.echo(f"设备名称: {device_name}, 密码: {password}, 描述: {desc}")
            global current_device, current_password
            current_device = device_name
            current_password = password
            create_frp_ini(device_name)
            run_frp_ini()
        else:
            typer.echo(f"设备密码错误！请检查密码是否正确")
    else:
        typer.echo(f"目前无法找到 {device_name}, 请检查设备名称是否正确")

if __name__ == "__main__":
    typer.run(main_cli)
