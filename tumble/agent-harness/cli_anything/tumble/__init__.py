import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('tumble running')
@cli.command()
def start(): click.echo('tumble started')
if __name__ == '__main__': cli()
