import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('twisted running')
@cli.command()
def start(): click.echo('twisted started')
if __name__ == '__main__': cli()
