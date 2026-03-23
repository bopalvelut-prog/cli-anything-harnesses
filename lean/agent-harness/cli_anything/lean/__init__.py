import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('lean running')
@cli.command()
def start(): click.echo('lean started')
if __name__ == '__main__': cli()
