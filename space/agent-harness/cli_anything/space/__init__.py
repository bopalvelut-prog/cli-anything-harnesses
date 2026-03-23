import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('space running')
@cli.command()
def start(): click.echo('space started')
if __name__ == '__main__': cli()
