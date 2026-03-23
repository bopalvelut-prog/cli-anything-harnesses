import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('subtitle running')
@cli.command()
def start(): click.echo('subtitle started')
if __name__ == '__main__': cli()
