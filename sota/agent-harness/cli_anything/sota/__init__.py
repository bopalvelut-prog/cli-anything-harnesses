import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('sota running')
@cli.command()
def start(): click.echo('sota started')
if __name__ == '__main__': cli()
