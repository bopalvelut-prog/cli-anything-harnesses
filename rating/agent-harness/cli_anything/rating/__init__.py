import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('rating running')
@cli.command()
def start(): click.echo('rating started')
if __name__ == '__main__': cli()
