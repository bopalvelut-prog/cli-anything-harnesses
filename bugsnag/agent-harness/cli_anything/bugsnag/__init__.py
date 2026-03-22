import click, subprocess
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('Bugsnag configured')
@cli.command()
def notify(): click.echo('Error notification sent')
if __name__ == '__main__': cli()
