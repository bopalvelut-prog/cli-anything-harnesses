import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pact running')
@cli.command()
def start(): click.echo('pact started')
if __name__ == '__main__': cli()
