import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('formal running')
@cli.command()
def start(): click.echo('formal started')
if __name__ == '__main__': cli()
