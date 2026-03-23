import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('tension running')
@cli.command()
def start(): click.echo('tension started')
if __name__ == '__main__': cli()
