import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('overcome running')
@cli.command()
def start(): click.echo('overcome started')
if __name__ == '__main__': cli()
