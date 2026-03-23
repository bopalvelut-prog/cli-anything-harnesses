import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('socket running')
@cli.command()
def start(): click.echo('socket started')
if __name__ == '__main__': cli()
