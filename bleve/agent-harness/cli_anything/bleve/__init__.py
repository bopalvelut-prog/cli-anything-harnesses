import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bleve running')
@cli.command()
def start(): click.echo('bleve started')
if __name__ == '__main__': cli()
