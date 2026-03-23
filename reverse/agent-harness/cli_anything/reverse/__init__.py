import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('reverse running')
@cli.command()
def start(): click.echo('reverse started')
if __name__ == '__main__': cli()
