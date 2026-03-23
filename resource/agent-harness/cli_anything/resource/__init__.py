import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('resource running')
@cli.command()
def start(): click.echo('resource started')
if __name__ == '__main__': cli()
