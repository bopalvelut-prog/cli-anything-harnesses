import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('quiet running')
@cli.command()
def start(): click.echo('quiet started')
if __name__ == '__main__': cli()
