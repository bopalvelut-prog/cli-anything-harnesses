import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('trouble running')
@cli.command()
def start(): click.echo('trouble started')
if __name__ == '__main__': cli()
