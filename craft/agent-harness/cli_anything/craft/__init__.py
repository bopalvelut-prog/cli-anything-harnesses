import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('craft running')
@cli.command()
def start(): click.echo('craft started')
if __name__ == '__main__': cli()
