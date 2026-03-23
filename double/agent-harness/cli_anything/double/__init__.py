import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('double running')
@cli.command()
def start(): click.echo('double started')
if __name__ == '__main__': cli()
