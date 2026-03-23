import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('email running')
@cli.command()
def start(): click.echo('email started')
if __name__ == '__main__': cli()
