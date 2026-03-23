import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('buildah running')
@cli.command()
def start(): click.echo('buildah started')
if __name__ == '__main__': cli()
