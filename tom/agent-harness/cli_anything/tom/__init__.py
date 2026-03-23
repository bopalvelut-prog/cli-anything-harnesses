import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('tom running')
@cli.command()
def start(): click.echo('tom started')
if __name__ == '__main__': cli()
