import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cilium running')
@cli.command()
def start(): click.echo('cilium started')
if __name__ == '__main__': cli()
