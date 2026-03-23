import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('force running')
@cli.command()
def start(): click.echo('force started')
if __name__ == '__main__': cli()
