import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('whole running')
@cli.command()
def start(): click.echo('whole started')
if __name__ == '__main__': cli()
