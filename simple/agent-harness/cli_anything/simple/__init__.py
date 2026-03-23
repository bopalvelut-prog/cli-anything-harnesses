import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('simple running')
@cli.command()
def start(): click.echo('simple started')
if __name__ == '__main__': cli()
