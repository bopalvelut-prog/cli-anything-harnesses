import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('tuck running')
@cli.command()
def start(): click.echo('tuck started')
if __name__ == '__main__': cli()
