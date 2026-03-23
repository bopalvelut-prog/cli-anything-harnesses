import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('main running')
@cli.command()
def start(): click.echo('main started')
if __name__ == '__main__': cli()
