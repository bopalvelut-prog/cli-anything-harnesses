import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ascender running')
@cli.command()
def start(): click.echo('ascender started')
if __name__ == '__main__': cli()
