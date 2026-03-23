import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('beauty running')
@cli.command()
def start(): click.echo('beauty started')
if __name__ == '__main__': cli()
