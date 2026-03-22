import click, subprocess
@click.group()
def cli(): pass
@cli.command()
@click.argument('name')
def status(name): subprocess.run(['systemctl', 'status', f'{name}.timer'])
@cli.command()
@click.argument('name')
def start(name): subprocess.run(['systemctl', 'start', f'{name}.timer'])
if __name__ == '__main__': cli()
