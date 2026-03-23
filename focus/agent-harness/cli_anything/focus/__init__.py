import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('focus running')
@cli.command()
def start(): click.echo('focus started')
if __name__ == '__main__': cli()
