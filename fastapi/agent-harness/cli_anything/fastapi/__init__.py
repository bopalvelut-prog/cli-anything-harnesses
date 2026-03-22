import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def dev(): subprocess.run(['fastapi', 'dev', 'main.py'])
@cli.command()
def run(): subprocess.run(['uvicorn', 'main:app'])
if __name__ == '__main__': cli()
