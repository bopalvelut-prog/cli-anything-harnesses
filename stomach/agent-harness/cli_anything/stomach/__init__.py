import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('stomach running')
@cli.command()
def start(): click.echo('stomach started')
if __name__ == '__main__': cli()
