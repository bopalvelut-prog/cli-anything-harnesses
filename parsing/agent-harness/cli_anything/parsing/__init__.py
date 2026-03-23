import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('parsing running')
@cli.command()
def start(): click.echo('parsing started')
if __name__ == '__main__': cli()
