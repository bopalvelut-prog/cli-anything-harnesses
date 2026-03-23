import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('united running')
@cli.command()
def start(): click.echo('united started')
if __name__ == '__main__': cli()
