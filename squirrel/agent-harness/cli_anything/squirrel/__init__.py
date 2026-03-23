import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('squirrel running')
@cli.command()
def start(): click.echo('squirrel started')
if __name__ == '__main__': cli()
