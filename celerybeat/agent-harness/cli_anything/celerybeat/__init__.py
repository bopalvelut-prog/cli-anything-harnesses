import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('celerybeat running')
@cli.command()
def start(): click.echo('celerybeat started')
if __name__ == '__main__': cli()
