import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sort running')
@cli.command()
def start(): click.echo('sort started')
if __name__ == '__main__': cli()
