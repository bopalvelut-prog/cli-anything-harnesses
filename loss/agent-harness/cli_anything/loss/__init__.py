import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('loss running')
@cli.command()
def start(): click.echo('loss started')
if __name__ == '__main__': cli()
