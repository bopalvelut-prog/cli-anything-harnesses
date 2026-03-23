import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('serve running')
@cli.command()
def start(): click.echo('serve started')
if __name__ == '__main__': cli()
