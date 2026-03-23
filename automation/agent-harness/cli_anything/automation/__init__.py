import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('automation running')
@cli.command()
def start(): click.echo('automation started')
if __name__ == '__main__': cli()
