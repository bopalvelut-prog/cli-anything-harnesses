import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('view running')
@cli.command()
def start(): click.echo('view started')
if __name__ == '__main__': cli()
