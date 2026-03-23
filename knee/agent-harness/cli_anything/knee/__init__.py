import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('knee running')
@cli.command()
def start(): click.echo('knee started')
if __name__ == '__main__': cli()
