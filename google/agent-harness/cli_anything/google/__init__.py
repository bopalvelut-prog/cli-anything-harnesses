import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('google running')
@cli.command()
def start(): click.echo('google started')
if __name__ == '__main__': cli()
