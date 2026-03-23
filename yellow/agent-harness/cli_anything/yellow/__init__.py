import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('yellow running')
@cli.command()
def start(): click.echo('yellow started')
if __name__ == '__main__': cli()
