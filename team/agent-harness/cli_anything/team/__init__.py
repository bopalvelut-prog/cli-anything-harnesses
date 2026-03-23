import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('team running')
@cli.command()
def start(): click.echo('team started')
if __name__ == '__main__': cli()
