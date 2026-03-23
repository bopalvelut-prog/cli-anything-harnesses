import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('thread running')
@cli.command()
def start(): click.echo('thread started')
if __name__ == '__main__': cli()
