import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('breath running')
@cli.command()
def start(): click.echo('breath started')
if __name__ == '__main__': cli()
