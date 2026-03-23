import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('kiwi running')
@cli.command()
def start(): click.echo('kiwi started')
if __name__ == '__main__': cli()
