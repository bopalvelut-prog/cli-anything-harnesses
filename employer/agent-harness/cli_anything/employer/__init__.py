import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('employer running')
@cli.command()
def start(): click.echo('employer started')
if __name__ == '__main__': cli()
