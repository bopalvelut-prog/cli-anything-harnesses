import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('pastebin running')
@cli.command()
def start(): click.echo('pastebin started')
if __name__ == '__main__': cli()
