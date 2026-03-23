import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('symbol running')
@cli.command()
def start(): click.echo('symbol started')
if __name__ == '__main__': cli()
