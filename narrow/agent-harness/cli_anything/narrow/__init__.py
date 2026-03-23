import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('narrow running')
@cli.command()
def start(): click.echo('narrow started')
if __name__ == '__main__': cli()
