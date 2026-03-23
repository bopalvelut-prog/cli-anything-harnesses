import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('meson running')
@cli.command()
def start(): click.echo('meson started')
if __name__ == '__main__': cli()
