import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('leaf running')
@cli.command()
def start(): click.echo('leaf started')
if __name__ == '__main__': cli()
