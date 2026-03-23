import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('monitor running')
@cli.command()
def start(): click.echo('monitor started')
if __name__ == '__main__': cli()
