import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('memray running')
@cli.command()
def start(): click.echo('memray started')
if __name__ == '__main__': cli()
