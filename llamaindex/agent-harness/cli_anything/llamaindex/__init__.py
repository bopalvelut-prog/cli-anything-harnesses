import click
@click.group()
def cli(): pass
@cli.command()
def query(): click.echo('LlamaIndex query')
@cli.command()
def index(): click.echo('LlamaIndex index')
if __name__ == '__main__': cli()
