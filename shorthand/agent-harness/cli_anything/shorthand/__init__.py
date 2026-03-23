import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('shorthand running')
@cli.command()
def start(): click.echo('shorthand started')
if __name__ == '__main__': cli()
