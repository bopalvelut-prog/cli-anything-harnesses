import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('title running')
@cli.command()
def start(): click.echo('title started')
if __name__ == '__main__': cli()
