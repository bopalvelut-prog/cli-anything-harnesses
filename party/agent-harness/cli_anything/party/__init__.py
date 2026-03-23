import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('party running')
@cli.command()
def start(): click.echo('party started')
if __name__ == '__main__': cli()
