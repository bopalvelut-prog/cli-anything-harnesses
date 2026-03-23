import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('challenge running')
@cli.command()
def start(): click.echo('challenge started')
if __name__ == '__main__': cli()
