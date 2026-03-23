import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('library running')
@cli.command()
def start(): click.echo('library started')
if __name__ == '__main__': cli()
