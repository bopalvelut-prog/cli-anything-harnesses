import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ark running')
@cli.command()
def start(): click.echo('ark started')
if __name__ == '__main__': cli()
