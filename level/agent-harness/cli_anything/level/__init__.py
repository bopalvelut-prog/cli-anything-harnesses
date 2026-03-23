import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('level running')
@cli.command()
def start(): click.echo('level started')
if __name__ == '__main__': cli()
