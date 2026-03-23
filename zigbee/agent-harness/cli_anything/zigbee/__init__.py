import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('zigbee running')
@cli.command()
def start(): click.echo('zigbee started')
if __name__ == '__main__': cli()
