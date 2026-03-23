import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('evil running')
@cli.command()
def start(): click.echo('evil started')
if __name__ == '__main__': cli()
