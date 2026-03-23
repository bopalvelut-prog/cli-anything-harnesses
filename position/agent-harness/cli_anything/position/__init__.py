import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('position running')
@cli.command()
def start(): click.echo('position started')
if __name__ == '__main__': cli()
