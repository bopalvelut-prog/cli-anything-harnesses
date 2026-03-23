import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ghci running')
@cli.command()
def start(): click.echo('ghci started')
if __name__ == '__main__': cli()
