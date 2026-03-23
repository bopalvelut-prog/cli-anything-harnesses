import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('dkms running')
@cli.command()
def start(): click.echo('dkms started')
if __name__ == '__main__': cli()
