import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('composable running')
@cli.command()
def start(): click.echo('composable started')
if __name__ == '__main__': cli()
