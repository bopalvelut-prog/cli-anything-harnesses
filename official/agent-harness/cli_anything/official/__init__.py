import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('official running')
@cli.command()
def start(): click.echo('official started')
if __name__ == '__main__': cli()
