import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def server(): subprocess.run(['ssserver', '-c', 'config.json'])
@cli.command()
def client(): subprocess.run(['sslocal', '-c', 'config.json'])
@cli.command()
def version(): subprocess.run(['sslocal', '--version'])
if __name__ == '__main__': cli()
