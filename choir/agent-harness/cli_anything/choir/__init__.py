import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('choir running')
@cli.command()
def start(): click.echo('choir started')
if __name__ == '__main__': cli()
