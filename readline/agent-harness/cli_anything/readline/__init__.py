import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('readline running')
@cli.command()
def start(): click.echo('readline started')
if __name__ == '__main__': cli()
