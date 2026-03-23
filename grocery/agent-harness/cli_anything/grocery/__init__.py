import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('grocery running')
@cli.command()
def start(): click.echo('grocery started')
if __name__ == '__main__': cli()
