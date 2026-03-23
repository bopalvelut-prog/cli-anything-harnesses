import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('commit running')
@cli.command()
def start(): click.echo('commit started')
if __name__ == '__main__': cli()
