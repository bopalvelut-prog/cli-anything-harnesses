import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('newspaper running')
@cli.command()
def start(): click.echo('newspaper started')
if __name__ == '__main__': cli()
