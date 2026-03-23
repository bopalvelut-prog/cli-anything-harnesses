import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('moderator running')
@cli.command()
def start(): click.echo('moderator started')
if __name__ == '__main__': cli()
