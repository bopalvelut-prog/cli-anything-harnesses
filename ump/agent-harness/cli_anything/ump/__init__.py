import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ump running')
@cli.command()
def start(): click.echo('ump started')
if __name__ == '__main__': cli()
