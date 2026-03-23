import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('fast running')
@cli.command()
def start(): click.echo('fast started')
if __name__ == '__main__': cli()
