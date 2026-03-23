import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('success running')
@cli.command()
def start(): click.echo('success started')
if __name__ == '__main__': cli()
