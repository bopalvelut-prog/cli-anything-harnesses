import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('zinc running')
@cli.command()
def start(): click.echo('zinc started')
if __name__ == '__main__': cli()
