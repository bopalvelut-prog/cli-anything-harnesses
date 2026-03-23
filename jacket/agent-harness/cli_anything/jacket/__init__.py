import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('jacket running')
@cli.command()
def start(): click.echo('jacket started')
if __name__ == '__main__': cli()
