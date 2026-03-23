import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('guarantee running')
@cli.command()
def start(): click.echo('guarantee started')
if __name__ == '__main__': cli()
