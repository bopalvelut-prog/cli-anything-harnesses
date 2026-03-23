import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('match running')
@cli.command()
def start(): click.echo('match started')
if __name__ == '__main__': cli()
