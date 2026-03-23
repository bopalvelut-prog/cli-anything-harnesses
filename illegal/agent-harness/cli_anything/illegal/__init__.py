import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('illegal running')
@cli.command()
def start(): click.echo('illegal started')
if __name__ == '__main__': cli()
