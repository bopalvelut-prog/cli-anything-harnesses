import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('shoe running')
@cli.command()
def start(): click.echo('shoe started')
if __name__ == '__main__': cli()
