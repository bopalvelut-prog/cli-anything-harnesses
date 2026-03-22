import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): subprocess.run(['clash', '-d', '.'])
@cli.command()
def version(): subprocess.run(['clash', '-v'])
@cli.command()
def test(): click.echo('Clash configuration test')
if __name__ == '__main__': cli()
