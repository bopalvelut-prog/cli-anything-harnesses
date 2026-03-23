import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('wage running')
@cli.command()
def start(): click.echo('wage started')
if __name__ == '__main__': cli()
