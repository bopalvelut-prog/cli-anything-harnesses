import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('lego running')
@cli.command()
def start(): click.echo('lego started')
if __name__ == '__main__': cli()
