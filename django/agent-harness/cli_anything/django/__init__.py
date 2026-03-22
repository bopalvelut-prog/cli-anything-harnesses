import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def run(): subprocess.run(['python', 'manage.py', 'runserver'])
@cli.command()
def migrate(): subprocess.run(['python', 'manage.py', 'migrate'])
if __name__ == '__main__': cli()
