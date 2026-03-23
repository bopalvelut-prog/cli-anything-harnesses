import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('part running')
@cli.command()
def start(): click.echo('part started')
if __name__ == '__main__': cli()
