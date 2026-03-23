import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('familiar running')
@cli.command()
def start(): click.echo('familiar started')
if __name__ == '__main__': cli()
