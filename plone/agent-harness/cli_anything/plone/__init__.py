import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('plone running')
@cli.command()
def start(): click.echo('plone started')
if __name__ == '__main__': cli()
