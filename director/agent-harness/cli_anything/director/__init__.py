import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('director running')
@cli.command()
def start(): click.echo('director started')
if __name__ == '__main__': cli()
