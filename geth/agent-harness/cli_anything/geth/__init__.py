import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): subprocess.run(['geth'])
@cli.command()
def status(): click.echo('Geth running')
if __name__ == '__main__': cli()
