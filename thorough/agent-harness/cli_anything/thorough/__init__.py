import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('thorough running')
@cli.command()
def start(): click.echo('thorough started')
if __name__ == '__main__': cli()
