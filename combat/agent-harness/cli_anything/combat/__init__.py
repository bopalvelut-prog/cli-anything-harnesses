import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('combat running')
@cli.command()
def start(): click.echo('combat started')
if __name__ == '__main__': cli()
