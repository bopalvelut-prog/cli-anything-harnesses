import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('selector running')
@cli.command()
def start(): click.echo('selector started')
if __name__ == '__main__': cli()
