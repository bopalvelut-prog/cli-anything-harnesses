import click
@click.group()
def cli(): pass
@cli.command()
def serve(): click.echo('Tabby serve')
@cli.command()
def code(): click.echo('Tabby code')
if __name__ == '__main__': cli()
