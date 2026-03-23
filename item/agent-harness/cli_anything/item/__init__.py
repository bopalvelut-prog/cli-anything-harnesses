import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('item running')
@cli.command()
def start(): click.echo('item started')
if __name__ == '__main__': cli()
