import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('forward running')
@cli.command()
def start(): click.echo('forward started')
if __name__ == '__main__': cli()
