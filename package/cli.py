import typer

def main(device_name: str):
    typer.echo(f"Hello {device_name}, ")

if __name__ == "__main__":
    typer.run(main)
