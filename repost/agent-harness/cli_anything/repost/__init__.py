import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('repost running')
@cli.command()
def start(): click.echo('repost started')
if __name__ == '__main__': cli()
