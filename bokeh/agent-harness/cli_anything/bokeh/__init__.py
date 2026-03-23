import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bokeh running')
@cli.command()
def start(): click.echo('bokeh started')
if __name__ == '__main__': cli()
