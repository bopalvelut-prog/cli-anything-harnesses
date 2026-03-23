import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('desperate running')
@cli.command()
def start(): click.echo('desperate started')
if __name__ == '__main__': cli()
