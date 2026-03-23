import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('axis running')
@cli.command()
def start(): click.echo('axis started')
if __name__ == '__main__': cli()
