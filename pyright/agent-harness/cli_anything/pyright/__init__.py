import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pyright running')
@cli.command()
def start(): click.echo('pyright started')
if __name__ == '__main__': cli()
