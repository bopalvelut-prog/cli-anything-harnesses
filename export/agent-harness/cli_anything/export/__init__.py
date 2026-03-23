import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('export running')
@cli.command()
def start(): click.echo('export started')
if __name__ == '__main__': cli()
