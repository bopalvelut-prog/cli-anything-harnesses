import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('extreme running')
@cli.command()
def start(): click.echo('extreme started')
if __name__ == '__main__': cli()
