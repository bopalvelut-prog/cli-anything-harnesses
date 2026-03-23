import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('second running')
@cli.command()
def start(): click.echo('second started')
if __name__ == '__main__': cli()
