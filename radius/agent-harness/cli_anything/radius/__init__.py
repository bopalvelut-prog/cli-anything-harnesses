import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('radius running')
@cli.command()
def start(): click.echo('radius started')
if __name__ == '__main__': cli()
