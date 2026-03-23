import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('armature running')
@cli.command()
def start(): click.echo('armature started')
if __name__ == '__main__': cli()
