import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('buffer running')
@cli.command()
def start(): click.echo('buffer started')
if __name__ == '__main__': cli()
