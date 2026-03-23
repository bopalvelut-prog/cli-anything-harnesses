import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('fact running')
@cli.command()
def start(): click.echo('fact started')
if __name__ == '__main__': cli()
