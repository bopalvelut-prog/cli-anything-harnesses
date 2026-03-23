import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mtu running')
@cli.command()
def start(): click.echo('mtu started')
if __name__ == '__main__': cli()
