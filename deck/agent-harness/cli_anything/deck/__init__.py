import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('deck running')
@cli.command()
def start(): click.echo('deck started')
if __name__ == '__main__': cli()
