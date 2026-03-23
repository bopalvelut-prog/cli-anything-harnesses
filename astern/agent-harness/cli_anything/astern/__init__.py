import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('astern running')
@cli.command()
def start(): click.echo('astern started')
if __name__ == '__main__': cli()
