import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('roll running')
@cli.command()
def start(): click.echo('roll started')
if __name__ == '__main__': cli()
