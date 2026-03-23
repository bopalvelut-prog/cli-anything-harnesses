import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('blue running')
@cli.command()
def start(): click.echo('blue started')
if __name__ == '__main__': cli()
