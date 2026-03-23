import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('messaging running')
@cli.command()
def start(): click.echo('messaging started')
if __name__ == '__main__': cli()
