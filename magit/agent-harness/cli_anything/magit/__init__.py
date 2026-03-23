import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('magit running')
@cli.command()
def start(): click.echo('magit started')
if __name__ == '__main__': cli()
