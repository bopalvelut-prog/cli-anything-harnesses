import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('free running')
@cli.command()
def start(): click.echo('free started')
if __name__ == '__main__': cli()
