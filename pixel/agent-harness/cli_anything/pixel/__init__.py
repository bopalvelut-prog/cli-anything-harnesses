import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pixel running')
@cli.command()
def start(): click.echo('pixel started')
if __name__ == '__main__': cli()
