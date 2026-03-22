import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('BookStack status')
@cli.command()
def books(): click.echo('BookStack books')
if __name__ == '__main__': cli()
