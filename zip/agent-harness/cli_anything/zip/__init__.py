import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('zip running')
@cli.command()
def start(): click.echo('zip started')
if __name__ == '__main__': cli()
