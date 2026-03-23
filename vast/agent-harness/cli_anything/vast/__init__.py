import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('vast running')
@cli.command()
def start(): click.echo('vast started')
if __name__ == '__main__': cli()
