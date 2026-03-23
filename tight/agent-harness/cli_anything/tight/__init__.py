import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('tight running')
@cli.command()
def start(): click.echo('tight started')
if __name__ == '__main__': cli()
