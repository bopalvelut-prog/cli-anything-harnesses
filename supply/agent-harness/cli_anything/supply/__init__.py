import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('supply running')
@cli.command()
def start(): click.echo('supply started')
if __name__ == '__main__': cli()
