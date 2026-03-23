import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('buck running')
@cli.command()
def start(): click.echo('buck started')
if __name__ == '__main__': cli()
