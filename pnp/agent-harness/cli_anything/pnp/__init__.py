import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pnp running')
@cli.command()
def start(): click.echo('pnp started')
if __name__ == '__main__': cli()
