import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sonobuoy running')
@cli.command()
def start(): click.echo('sonobuoy started')
if __name__ == '__main__': cli()
