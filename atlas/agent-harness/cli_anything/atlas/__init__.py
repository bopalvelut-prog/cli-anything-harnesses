import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('atlas running')
@cli.command()
def start(): click.echo('atlas started')
if __name__ == '__main__': cli()
