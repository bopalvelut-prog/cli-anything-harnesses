import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('tunnel running')
@cli.command()
def start(): click.echo('tunnel started')
if __name__ == '__main__': cli()
