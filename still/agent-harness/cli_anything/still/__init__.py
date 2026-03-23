import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('still running')
@cli.command()
def start(): click.echo('still started')
if __name__ == '__main__': cli()
