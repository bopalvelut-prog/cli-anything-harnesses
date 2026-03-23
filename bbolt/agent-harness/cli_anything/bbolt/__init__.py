import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('bbolt running')
@cli.command()
def start(): click.echo('bbolt started')
if __name__ == '__main__': cli()
