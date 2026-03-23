import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('chief running')
@cli.command()
def start(): click.echo('chief started')
if __name__ == '__main__': cli()
