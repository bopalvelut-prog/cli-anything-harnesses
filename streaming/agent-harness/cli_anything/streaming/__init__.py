import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('streaming running')
@cli.command()
def start(): click.echo('streaming started')
if __name__ == '__main__': cli()
