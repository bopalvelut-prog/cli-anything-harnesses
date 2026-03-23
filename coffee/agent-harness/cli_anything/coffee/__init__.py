import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('coffee running')
@cli.command()
def start(): click.echo('coffee started')
if __name__ == '__main__': cli()
