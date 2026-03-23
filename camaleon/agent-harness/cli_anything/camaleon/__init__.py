import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('camaleon running')
@cli.command()
def start(): click.echo('camaleon started')
if __name__ == '__main__': cli()
