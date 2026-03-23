import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('script running')
@cli.command()
def start(): click.echo('script started')
if __name__ == '__main__': cli()
