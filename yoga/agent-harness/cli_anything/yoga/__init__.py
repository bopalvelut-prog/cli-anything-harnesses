import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('yoga running')
@cli.command()
def start(): click.echo('yoga started')
if __name__ == '__main__': cli()
