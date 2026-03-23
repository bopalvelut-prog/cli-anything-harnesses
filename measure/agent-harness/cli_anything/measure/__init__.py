import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('measure running')
@cli.command()
def start(): click.echo('measure started')
if __name__ == '__main__': cli()
