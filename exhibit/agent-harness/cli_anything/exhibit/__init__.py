import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('exhibit running')
@cli.command()
def start(): click.echo('exhibit started')
if __name__ == '__main__': cli()
