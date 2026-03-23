import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('asia running')
@cli.command()
def start(): click.echo('asia started')
if __name__ == '__main__': cli()
