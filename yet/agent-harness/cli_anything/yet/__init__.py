import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('yet running')
@cli.command()
def start(): click.echo('yet started')
if __name__ == '__main__': cli()
