import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('super running')
@cli.command()
def start(): click.echo('super started')
if __name__ == '__main__': cli()
