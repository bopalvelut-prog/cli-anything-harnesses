import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('shop running')
@cli.command()
def start(): click.echo('shop started')
if __name__ == '__main__': cli()
