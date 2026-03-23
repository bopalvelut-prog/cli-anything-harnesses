import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('openstack running')
@cli.command()
def start(): click.echo('openstack started')
if __name__ == '__main__': cli()
