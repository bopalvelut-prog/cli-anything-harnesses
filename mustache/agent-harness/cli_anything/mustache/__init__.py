import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('mustache running')
@cli.command()
def start(): click.echo('mustache started')
if __name__ == '__main__': cli()
