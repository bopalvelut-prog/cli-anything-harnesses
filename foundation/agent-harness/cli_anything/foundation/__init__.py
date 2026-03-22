import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def list(): click.echo('Foundation listings')
@cli.command()
def buy(): click.echo('Foundation buy')
if __name__ == '__main__': cli()
