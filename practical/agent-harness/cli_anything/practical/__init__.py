import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('practical running')
@cli.command()
def start(): click.echo('practical started')
if __name__ == '__main__': cli()
