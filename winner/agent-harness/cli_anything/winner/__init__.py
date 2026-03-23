import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('winner running')
@cli.command()
def start(): click.echo('winner started')
if __name__ == '__main__': cli()
