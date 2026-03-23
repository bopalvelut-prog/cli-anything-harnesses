import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('round running')
@cli.command()
def start(): click.echo('round started')
if __name__ == '__main__': cli()
