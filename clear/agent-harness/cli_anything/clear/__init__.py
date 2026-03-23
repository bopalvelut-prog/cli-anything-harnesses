import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('clear running')
@cli.command()
def start(): click.echo('clear started')
if __name__ == '__main__': cli()
