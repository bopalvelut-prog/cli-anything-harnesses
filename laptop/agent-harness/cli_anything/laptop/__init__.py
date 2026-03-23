import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('laptop running')
@cli.command()
def start(): click.echo('laptop started')
if __name__ == '__main__': cli()
