import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('rom running')
@cli.command()
def start(): click.echo('rom started')
if __name__ == '__main__': cli()
