import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('xargs running')
@cli.command()
def start(): click.echo('xargs started')
if __name__ == '__main__': cli()
