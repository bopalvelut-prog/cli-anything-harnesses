import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bread running')
@cli.command()
def start(): click.echo('bread started')
if __name__ == '__main__': cli()
