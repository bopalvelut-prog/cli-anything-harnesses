import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def migrate(): subprocess.run(['flyway', 'migrate'])
@cli.command()
def info(): subprocess.run(['flyway', 'info'])
if __name__ == '__main__': cli()
