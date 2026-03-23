import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('increase running')
@cli.command()
def start(): click.echo('increase started')
if __name__ == '__main__': cli()
