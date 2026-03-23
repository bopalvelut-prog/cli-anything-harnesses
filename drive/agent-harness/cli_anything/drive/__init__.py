import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('drive running')
@cli.command()
def start(): click.echo('drive started')
if __name__ == '__main__': cli()
