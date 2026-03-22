import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('OpenCMS running')
@cli.command()
def pages(): click.echo('OpenCMS pages')
if __name__ == '__main__': cli()
