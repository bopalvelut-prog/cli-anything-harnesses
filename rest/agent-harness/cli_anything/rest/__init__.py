import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('rest running')
@cli.command()
def start(): click.echo('rest started')
if __name__ == '__main__': cli()
