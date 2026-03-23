import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('strip running')
@cli.command()
def start(): click.echo('strip started')
if __name__ == '__main__': cli()
