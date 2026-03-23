import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('paclink running')
@cli.command()
def start(): click.echo('paclink started')
if __name__ == '__main__': cli()
