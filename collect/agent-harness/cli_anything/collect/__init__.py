import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('collect running')
@cli.command()
def start(): click.echo('collect started')
if __name__ == '__main__': cli()
