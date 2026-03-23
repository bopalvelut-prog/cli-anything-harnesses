import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('villa running')
@cli.command()
def start(): click.echo('villa started')
if __name__ == '__main__': cli()
