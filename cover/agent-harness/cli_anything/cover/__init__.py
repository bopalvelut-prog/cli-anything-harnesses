import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('cover running')
@cli.command()
def start(): click.echo('cover started')
if __name__ == '__main__': cli()
