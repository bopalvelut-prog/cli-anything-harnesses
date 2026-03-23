import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('permalinks running')
@cli.command()
def start(): click.echo('permalinks started')
if __name__ == '__main__': cli()
