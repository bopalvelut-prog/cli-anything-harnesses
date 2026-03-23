import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('transport running')
@cli.command()
def start(): click.echo('transport started')
if __name__ == '__main__': cli()
