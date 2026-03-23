import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('reader running')
@cli.command()
def start(): click.echo('reader started')
if __name__ == '__main__': cli()
