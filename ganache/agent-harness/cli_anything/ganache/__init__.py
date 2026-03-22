import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def start(): subprocess.run(['ganache-cli'])
@cli.command()
def status(): click.echo('Ganache running')
if __name__ == '__main__': cli()
