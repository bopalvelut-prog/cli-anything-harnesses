import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('offend running')
@cli.command()
def start(): click.echo('offend started')
if __name__ == '__main__': cli()
