import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('advisor running')
@cli.command()
def start(): click.echo('advisor started')
if __name__ == '__main__': cli()
