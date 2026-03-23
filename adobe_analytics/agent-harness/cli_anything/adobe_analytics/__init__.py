import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('adobe_analytics running')
@cli.command()
def start(): click.echo('adobe_analytics started')
if __name__ == '__main__': cli()
