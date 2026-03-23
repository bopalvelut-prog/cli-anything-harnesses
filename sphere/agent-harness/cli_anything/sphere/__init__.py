import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sphere running')
@cli.command()
def start(): click.echo('sphere started')
if __name__ == '__main__': cli()
