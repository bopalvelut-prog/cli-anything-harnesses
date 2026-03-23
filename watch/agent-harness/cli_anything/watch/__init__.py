import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('watch running')
@cli.command()
def start(): click.echo('watch started')
if __name__ == '__main__': cli()
