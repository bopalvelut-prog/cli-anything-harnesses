import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('accuweather running')
@cli.command()
def start(): click.echo('accuweather started')
if __name__ == '__main__': cli()
