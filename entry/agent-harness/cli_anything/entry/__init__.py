import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('entry running')
@cli.command()
def start(): click.echo('entry started')
if __name__ == '__main__': cli()
