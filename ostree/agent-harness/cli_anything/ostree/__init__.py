import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ostree running')
@cli.command()
def start(): click.echo('ostree started')
if __name__ == '__main__': cli()
