import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('world running')
@cli.command()
def start(): click.echo('world started')
if __name__ == '__main__': cli()
