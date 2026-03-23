import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('aegis running')
@cli.command()
def start(): click.echo('aegis started')
if __name__ == '__main__': cli()
