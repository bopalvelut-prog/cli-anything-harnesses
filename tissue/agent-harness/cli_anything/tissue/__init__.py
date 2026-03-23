import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('tissue running')
@cli.command()
def start(): click.echo('tissue started')
if __name__ == '__main__': cli()
