import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('spring running')
@cli.command()
def start(): click.echo('spring started')
if __name__ == '__main__': cli()
