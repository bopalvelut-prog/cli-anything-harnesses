import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('touch running')
@cli.command()
def start(): click.echo('touch started')
if __name__ == '__main__': cli()
