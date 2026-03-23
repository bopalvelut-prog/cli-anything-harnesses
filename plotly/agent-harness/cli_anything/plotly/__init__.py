import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('plotly running')
@cli.command()
def start(): click.echo('plotly started')
if __name__ == '__main__': cli()
