import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ping running')
@cli.command()
def start(): click.echo('ping started')
if __name__ == '__main__': cli()
