import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('remarkable running')
@cli.command()
def start(): click.echo('remarkable started')
if __name__ == '__main__': cli()
