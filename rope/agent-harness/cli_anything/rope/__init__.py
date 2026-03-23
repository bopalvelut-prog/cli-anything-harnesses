import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('rope running')
@cli.command()
def start(): click.echo('rope started')
if __name__ == '__main__': cli()
