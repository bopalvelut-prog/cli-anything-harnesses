import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('glad running')
@cli.command()
def start(): click.echo('glad started')
if __name__ == '__main__': cli()
