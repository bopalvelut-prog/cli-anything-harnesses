import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('upgrade running')
@cli.command()
def start(): click.echo('upgrade started')
if __name__ == '__main__': cli()
