import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('fulcio running')
@cli.command()
def start(): click.echo('fulcio started')
if __name__ == '__main__': cli()
