import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('asio running')
@cli.command()
def start(): click.echo('asio started')
if __name__ == '__main__': cli()
