import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('computer running')
@cli.command()
def start(): click.echo('computer started')
if __name__ == '__main__': cli()
