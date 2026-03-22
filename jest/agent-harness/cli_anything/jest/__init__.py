import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def test(): subprocess.run(['jest'])
@cli.command()
def watch(): subprocess.run(['jest', '--watch'])
@cli.command()
def coverage(): subprocess.run(['jest', '--coverage'])
@cli.command()
@click.argument('file')
def run(file): subprocess.run(['jest', file])
if __name__ == '__main__': cli()
