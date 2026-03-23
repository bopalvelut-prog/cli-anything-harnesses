import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('dolt running')
@cli.command()
def start(): click.echo('dolt started')
if __name__ == '__main__': cli()
