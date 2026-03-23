import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('profile running')
@cli.command()
def start(): click.echo('profile started')
if __name__ == '__main__': cli()
