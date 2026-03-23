import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('shelve running')
@cli.command()
def start(): click.echo('shelve started')
if __name__ == '__main__': cli()
