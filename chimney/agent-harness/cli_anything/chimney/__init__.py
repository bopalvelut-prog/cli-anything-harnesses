import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('chimney running')
@cli.command()
def start(): click.echo('chimney started')
if __name__ == '__main__': cli()
