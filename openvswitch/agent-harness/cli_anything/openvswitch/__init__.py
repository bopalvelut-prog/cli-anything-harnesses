import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('openvswitch running')
@cli.command()
def start(): click.echo('openvswitch started')
if __name__ == '__main__': cli()
