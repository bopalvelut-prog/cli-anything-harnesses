import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('investigate running')
@cli.command()
def start(): click.echo('investigate started')
if __name__ == '__main__': cli()
