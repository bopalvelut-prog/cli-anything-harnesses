import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('amundsen running')
@cli.command()
def start(): click.echo('amundsen started')
if __name__ == '__main__': cli()
