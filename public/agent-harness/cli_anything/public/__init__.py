import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('public running')
@cli.command()
def start(): click.echo('public started')
if __name__ == '__main__': cli()
