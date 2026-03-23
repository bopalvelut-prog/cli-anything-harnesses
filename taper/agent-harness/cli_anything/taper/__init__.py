import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('taper running')
@cli.command()
def start(): click.echo('taper started')
if __name__ == '__main__': cli()
