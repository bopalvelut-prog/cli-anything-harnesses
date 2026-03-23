import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('crucial running')
@cli.command()
def start(): click.echo('crucial started')
if __name__ == '__main__': cli()
