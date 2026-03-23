import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('link running')
@cli.command()
def start(): click.echo('link started')
if __name__ == '__main__': cli()
