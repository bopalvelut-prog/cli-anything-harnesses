import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('tiny running')
@cli.command()
def start(): click.echo('tiny started')
if __name__ == '__main__': cli()
