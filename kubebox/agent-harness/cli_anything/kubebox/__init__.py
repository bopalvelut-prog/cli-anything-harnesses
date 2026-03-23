import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('kubebox running')
@cli.command()
def start(): click.echo('kubebox started')
if __name__ == '__main__': cli()
