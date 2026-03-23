import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('wonder running')
@cli.command()
def start(): click.echo('wonder started')
if __name__ == '__main__': cli()
