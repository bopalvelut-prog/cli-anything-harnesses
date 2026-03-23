import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('nutanix running')
@cli.command()
def start(): click.echo('nutanix started')
if __name__ == '__main__': cli()
