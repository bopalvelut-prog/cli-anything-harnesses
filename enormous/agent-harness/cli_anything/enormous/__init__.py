import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('enormous running')
@cli.command()
def start(): click.echo('enormous started')
if __name__ == '__main__': cli()
