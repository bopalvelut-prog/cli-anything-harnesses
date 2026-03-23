import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('kraft running')
@cli.command()
def start(): click.echo('kraft started')
if __name__ == '__main__': cli()
