import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def test(): subprocess.run(['mocha'])
@cli.command()
def watch(): subprocess.run(['mocha', '--watch'])
@cli.command()
def cover(): subprocess.run(['nyc', 'mocha'])
if __name__ == '__main__': cli()
