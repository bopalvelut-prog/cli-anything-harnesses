import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('little running')
@cli.command()
def start(): click.echo('little started')
if __name__ == '__main__': cli()
