import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bend running')
@cli.command()
def start(): click.echo('bend started')
if __name__ == '__main__': cli()
