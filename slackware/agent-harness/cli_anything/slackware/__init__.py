import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('slackware running')
@cli.command()
def start(): click.echo('slackware started')
if __name__ == '__main__': cli()
