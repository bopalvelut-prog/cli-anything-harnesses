import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('article running')
@cli.command()
def start(): click.echo('article started')
if __name__ == '__main__': cli()
