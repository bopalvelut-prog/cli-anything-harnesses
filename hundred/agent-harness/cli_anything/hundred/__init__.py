import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('hundred running')
@cli.command()
def start(): click.echo('hundred started')
if __name__ == '__main__': cli()
