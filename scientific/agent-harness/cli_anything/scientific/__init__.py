import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('scientific running')
@cli.command()
def start(): click.echo('scientific started')
if __name__ == '__main__': cli()
