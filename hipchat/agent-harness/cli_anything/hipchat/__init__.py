import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('hipchat running')
@cli.command()
def start(): click.echo('hipchat started')
if __name__ == '__main__': cli()
