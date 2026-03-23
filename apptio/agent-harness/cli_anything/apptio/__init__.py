import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('apptio running')
@cli.command()
def start(): click.echo('apptio started')
if __name__ == '__main__': cli()
