import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Kentico running')
@cli.command()
def pages(): click.echo('Kentico pages')
if __name__ == '__main__': cli()
