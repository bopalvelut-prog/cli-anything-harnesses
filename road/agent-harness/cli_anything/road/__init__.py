import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('road running')
@cli.command()
def start(): click.echo('road started')
if __name__ == '__main__': cli()
