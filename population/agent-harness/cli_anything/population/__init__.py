import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('population running')
@cli.command()
def start(): click.echo('population started')
if __name__ == '__main__': cli()
