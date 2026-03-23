import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('archive running')
@cli.command()
def start(): click.echo('archive started')
if __name__ == '__main__': cli()
