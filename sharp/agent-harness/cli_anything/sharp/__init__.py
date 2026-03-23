import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sharp running')
@cli.command()
def start(): click.echo('sharp started')
if __name__ == '__main__': cli()
