import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('evening running')
@cli.command()
def start(): click.echo('evening started')
if __name__ == '__main__': cli()
