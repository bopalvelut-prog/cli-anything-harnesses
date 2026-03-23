import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('permission running')
@cli.command()
def start(): click.echo('permission started')
if __name__ == '__main__': cli()
