import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('jclouds running')
@cli.command()
def start(): click.echo('jclouds started')
if __name__ == '__main__': cli()
