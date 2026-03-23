import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('contact running')
@cli.command()
def start(): click.echo('contact started')
if __name__ == '__main__': cli()
