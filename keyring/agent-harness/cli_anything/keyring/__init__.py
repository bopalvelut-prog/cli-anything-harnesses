import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('keyring running')
@cli.command()
def start(): click.echo('keyring started')
if __name__ == '__main__': cli()
