import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('liquid running')
@cli.command()
def start(): click.echo('liquid started')
if __name__ == '__main__': cli()
