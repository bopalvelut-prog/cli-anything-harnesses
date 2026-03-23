import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('xxhash running')
@cli.command()
def start(): click.echo('xxhash started')
if __name__ == '__main__': cli()
