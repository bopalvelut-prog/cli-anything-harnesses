import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('libsodium running')
@cli.command()
def start(): click.echo('libsodium started')
if __name__ == '__main__': cli()
