import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('safety running')
@cli.command()
def start(): click.echo('safety started')
if __name__ == '__main__': cli()
