import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('db2 running')
@cli.command()
def start(): click.echo('db2 started')
if __name__ == '__main__': cli()
