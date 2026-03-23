import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('action running')
@cli.command()
def start(): click.echo('action started')
if __name__ == '__main__': cli()
