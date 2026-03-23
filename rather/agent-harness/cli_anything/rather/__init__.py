import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('rather running')
@cli.command()
def start(): click.echo('rather started')
if __name__ == '__main__': cli()
