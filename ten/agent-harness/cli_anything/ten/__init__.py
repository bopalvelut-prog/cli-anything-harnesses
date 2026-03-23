import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ten running')
@cli.command()
def start(): click.echo('ten started')
if __name__ == '__main__': cli()
