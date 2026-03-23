import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('nokia running')
@cli.command()
def start(): click.echo('nokia started')
if __name__ == '__main__': cli()
