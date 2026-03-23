import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('progress running')
@cli.command()
def start(): click.echo('progress started')
if __name__ == '__main__': cli()
