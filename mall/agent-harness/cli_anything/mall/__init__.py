import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mall running')
@cli.command()
def start(): click.echo('mall started')
if __name__ == '__main__': cli()
