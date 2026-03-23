import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('weather running')
@cli.command()
def start(): click.echo('weather started')
if __name__ == '__main__': cli()
