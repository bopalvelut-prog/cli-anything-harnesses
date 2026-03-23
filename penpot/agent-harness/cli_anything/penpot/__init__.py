import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('penpot running')
@cli.command()
def start(): click.echo('penpot started')
if __name__ == '__main__': cli()
