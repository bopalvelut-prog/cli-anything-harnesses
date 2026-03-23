import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('particular running')
@cli.command()
def start(): click.echo('particular started')
if __name__ == '__main__': cli()
