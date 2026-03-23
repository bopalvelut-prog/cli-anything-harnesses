import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('yours running')
@cli.command()
def start(): click.echo('yours started')
if __name__ == '__main__': cli()
