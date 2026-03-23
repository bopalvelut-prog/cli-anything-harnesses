import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('joy running')
@cli.command()
def start(): click.echo('joy started')
if __name__ == '__main__': cli()
