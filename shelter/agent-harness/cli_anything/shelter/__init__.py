import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('shelter running')
@cli.command()
def start(): click.echo('shelter started')
if __name__ == '__main__': cli()
