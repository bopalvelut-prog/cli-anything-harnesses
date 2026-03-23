import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('dedupe running')
@cli.command()
def start(): click.echo('dedupe started')
if __name__ == '__main__': cli()
