import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('applescript running')
@cli.command()
def start(): click.echo('applescript started')
if __name__ == '__main__': cli()
