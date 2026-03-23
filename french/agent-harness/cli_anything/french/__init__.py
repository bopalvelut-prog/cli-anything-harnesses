import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('french running')
@cli.command()
def start(): click.echo('french started')
if __name__ == '__main__': cli()
