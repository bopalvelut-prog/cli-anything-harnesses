import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('spike running')
@cli.command()
def start(): click.echo('spike started')
if __name__ == '__main__': cli()
