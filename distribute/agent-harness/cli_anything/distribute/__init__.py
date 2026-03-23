import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('distribute running')
@cli.command()
def start(): click.echo('distribute started')
if __name__ == '__main__': cli()
