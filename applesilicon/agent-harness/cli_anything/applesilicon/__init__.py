import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('applesilicon running')
@cli.command()
def start(): click.echo('applesilicon started')
if __name__ == '__main__': cli()
