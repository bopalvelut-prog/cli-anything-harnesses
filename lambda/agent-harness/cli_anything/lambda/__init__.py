import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('lambda running')
@cli.command()
def start(): click.echo('lambda started')
if __name__ == '__main__': cli()
