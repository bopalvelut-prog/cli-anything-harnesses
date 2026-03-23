import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('origin running')
@cli.command()
def start(): click.echo('origin started')
if __name__ == '__main__': cli()
