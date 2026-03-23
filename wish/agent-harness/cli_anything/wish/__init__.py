import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('wish running')
@cli.command()
def start(): click.echo('wish started')
if __name__ == '__main__': cli()
