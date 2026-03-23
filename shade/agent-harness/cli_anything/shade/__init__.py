import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('shade running')
@cli.command()
def start(): click.echo('shade started')
if __name__ == '__main__': cli()
