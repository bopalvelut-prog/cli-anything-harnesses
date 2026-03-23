import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('village running')
@cli.command()
def start(): click.echo('village started')
if __name__ == '__main__': cli()
