import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('rhythm running')
@cli.command()
def start(): click.echo('rhythm started')
if __name__ == '__main__': cli()
