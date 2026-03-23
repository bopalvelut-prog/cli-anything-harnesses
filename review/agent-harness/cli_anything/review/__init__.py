import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('review running')
@cli.command()
def start(): click.echo('review started')
if __name__ == '__main__': cli()
