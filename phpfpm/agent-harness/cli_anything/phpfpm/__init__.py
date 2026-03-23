import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('phpfpm running')
@cli.command()
def start(): click.echo('phpfpm started')
if __name__ == '__main__': cli()
