import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('creature running')
@cli.command()
def start(): click.echo('creature started')
if __name__ == '__main__': cli()
