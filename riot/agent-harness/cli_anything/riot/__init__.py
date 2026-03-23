import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('riot running')
@cli.command()
def start(): click.echo('riot started')
if __name__ == '__main__': cli()
