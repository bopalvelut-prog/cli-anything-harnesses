import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('xdp running')
@cli.command()
def start(): click.echo('xdp started')
if __name__ == '__main__': cli()
