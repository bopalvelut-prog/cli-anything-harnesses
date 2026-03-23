import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('logzio running')
@cli.command()
def start(): click.echo('logzio started')
if __name__ == '__main__': cli()
