import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('authorize running')
@cli.command()
def start(): click.echo('authorize started')
if __name__ == '__main__': cli()
