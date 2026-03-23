import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('dear running')
@cli.command()
def start(): click.echo('dear started')
if __name__ == '__main__': cli()
