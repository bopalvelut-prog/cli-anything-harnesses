import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('tragedy running')
@cli.command()
def start(): click.echo('tragedy started')
if __name__ == '__main__': cli()
