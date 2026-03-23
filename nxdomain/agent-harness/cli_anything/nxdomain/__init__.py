import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('nxdomain running')
@cli.command()
def start(): click.echo('nxdomain started')
if __name__ == '__main__': cli()
