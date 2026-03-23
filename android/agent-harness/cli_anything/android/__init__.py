import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('android running')
@cli.command()
def start(): click.echo('android started')
if __name__ == '__main__': cli()
