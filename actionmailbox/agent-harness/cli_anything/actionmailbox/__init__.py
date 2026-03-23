import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('actionmailbox running')
@cli.command()
def start(): click.echo('actionmailbox started')
if __name__ == '__main__': cli()
