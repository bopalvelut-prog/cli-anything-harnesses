import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('romantic running')
@cli.command()
def start(): click.echo('romantic started')
if __name__ == '__main__': cli()
