import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('dispatch running')
@cli.command()
def start(): click.echo('dispatch started')
if __name__ == '__main__': cli()
