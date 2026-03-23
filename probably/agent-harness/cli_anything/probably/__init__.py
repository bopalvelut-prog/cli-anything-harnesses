import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('probably running')
@cli.command()
def start(): click.echo('probably started')
if __name__ == '__main__': cli()
