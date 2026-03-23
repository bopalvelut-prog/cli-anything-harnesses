import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pscale running')
@cli.command()
def start(): click.echo('pscale started')
if __name__ == '__main__': cli()
