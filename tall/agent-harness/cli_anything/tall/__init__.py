import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('tall running')
@cli.command()
def start(): click.echo('tall started')
if __name__ == '__main__': cli()
