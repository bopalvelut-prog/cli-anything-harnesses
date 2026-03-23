import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('unlink running')
@cli.command()
def start(): click.echo('unlink started')
if __name__ == '__main__': cli()
