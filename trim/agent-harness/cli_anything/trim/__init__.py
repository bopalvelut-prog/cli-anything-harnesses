import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('trim running')
@cli.command()
def start(): click.echo('trim started')
if __name__ == '__main__': cli()
