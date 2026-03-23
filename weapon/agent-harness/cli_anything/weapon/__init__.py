import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('weapon running')
@cli.command()
def start(): click.echo('weapon started')
if __name__ == '__main__': cli()
