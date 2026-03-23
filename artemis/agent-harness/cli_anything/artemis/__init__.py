import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('artemis running')
@cli.command()
def start(): click.echo('artemis started')
if __name__ == '__main__': cli()
