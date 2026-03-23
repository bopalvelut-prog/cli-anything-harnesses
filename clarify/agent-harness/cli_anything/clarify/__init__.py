import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('clarify running')
@cli.command()
def start(): click.echo('clarify started')
if __name__ == '__main__': cli()
