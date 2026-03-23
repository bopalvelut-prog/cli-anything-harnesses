import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('vivid running')
@cli.command()
def start(): click.echo('vivid started')
if __name__ == '__main__': cli()
