import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('zoo running')
@cli.command()
def start(): click.echo('zoo started')
if __name__ == '__main__': cli()
