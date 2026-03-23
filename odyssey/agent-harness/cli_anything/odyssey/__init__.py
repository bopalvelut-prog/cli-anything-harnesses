import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('odyssey running')
@cli.command()
def start(): click.echo('odyssey started')
if __name__ == '__main__': cli()
