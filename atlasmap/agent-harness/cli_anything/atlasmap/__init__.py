import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('atlasmap running')
@cli.command()
def start(): click.echo('atlasmap started')
if __name__ == '__main__': cli()
