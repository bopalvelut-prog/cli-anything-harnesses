import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('revolution running')
@cli.command()
def start(): click.echo('revolution started')
if __name__ == '__main__': cli()
