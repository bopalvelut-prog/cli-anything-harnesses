import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('trivial running')
@cli.command()
def start(): click.echo('trivial started')
if __name__ == '__main__': cli()
