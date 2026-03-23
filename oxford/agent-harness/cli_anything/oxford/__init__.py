import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('oxford running')
@cli.command()
def start(): click.echo('oxford started')
if __name__ == '__main__': cli()
