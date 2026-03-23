import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mcp running')
@cli.command()
def start(): click.echo('mcp started')
if __name__ == '__main__': cli()
