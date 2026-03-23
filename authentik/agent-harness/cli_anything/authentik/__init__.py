import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('authentik running')
@cli.command()
def start(): click.echo('authentik started')
if __name__ == '__main__': cli()
