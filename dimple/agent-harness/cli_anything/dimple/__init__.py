import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('dimple running')
@cli.command()
def start(): click.echo('dimple started')
if __name__ == '__main__': cli()
