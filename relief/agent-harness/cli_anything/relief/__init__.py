import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('relief running')
@cli.command()
def start(): click.echo('relief started')
if __name__ == '__main__': cli()
