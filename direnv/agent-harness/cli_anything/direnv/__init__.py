import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('direnv running')
@cli.command()
def start(): click.echo('direnv started')
if __name__ == '__main__': cli()
