import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('udp running')
@cli.command()
def start(): click.echo('udp started')
if __name__ == '__main__': cli()
