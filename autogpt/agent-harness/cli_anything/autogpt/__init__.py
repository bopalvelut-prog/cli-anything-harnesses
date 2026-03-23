import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('autogpt running')
@cli.command()
def start(): click.echo('autogpt started')
if __name__ == '__main__': cli()
