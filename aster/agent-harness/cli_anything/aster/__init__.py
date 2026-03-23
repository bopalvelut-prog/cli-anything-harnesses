import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('aster running')
@cli.command()
def start(): click.echo('aster started')
if __name__ == '__main__': cli()
