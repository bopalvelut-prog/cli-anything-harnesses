import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('limit running')
@cli.command()
def start(): click.echo('limit started')
if __name__ == '__main__': cli()
