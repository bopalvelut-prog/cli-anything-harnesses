import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('flavor running')
@cli.command()
def start(): click.echo('flavor started')
if __name__ == '__main__': cli()
