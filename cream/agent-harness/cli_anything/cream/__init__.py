import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cream running')
@cli.command()
def start(): click.echo('cream started')
if __name__ == '__main__': cli()
