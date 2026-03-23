import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('error running')
@cli.command()
def start(): click.echo('error started')
if __name__ == '__main__': cli()
