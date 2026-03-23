import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('prefer running')
@cli.command()
def start(): click.echo('prefer started')
if __name__ == '__main__': cli()
