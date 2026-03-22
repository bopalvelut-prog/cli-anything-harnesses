import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def list(): click.echo('SuperRare listings')
@cli.command()
def buy(): click.echo('SuperRare buy')
if __name__ == '__main__': cli()
