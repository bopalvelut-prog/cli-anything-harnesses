import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('fantasy running')
@cli.command()
def start(): click.echo('fantasy started')
if __name__ == '__main__': cli()
