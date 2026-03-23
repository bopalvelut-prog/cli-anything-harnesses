import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('phrase running')
@cli.command()
def start(): click.echo('phrase started')
if __name__ == '__main__': cli()
