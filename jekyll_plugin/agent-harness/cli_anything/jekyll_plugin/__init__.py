import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('jekyll_plugin running')
@cli.command()
def start(): click.echo('jekyll_plugin started')
if __name__ == '__main__': cli()
