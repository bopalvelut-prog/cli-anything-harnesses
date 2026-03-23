import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('share running')
@cli.command()
def start(): click.echo('share started')
if __name__ == '__main__': cli()
