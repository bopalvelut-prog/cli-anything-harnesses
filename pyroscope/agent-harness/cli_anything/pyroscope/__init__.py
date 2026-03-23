import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pyroscope running')
@cli.command()
def start(): click.echo('pyroscope started')
if __name__ == '__main__': cli()
