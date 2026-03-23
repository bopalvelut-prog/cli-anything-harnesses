import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('territory running')
@cli.command()
def start(): click.echo('territory started')
if __name__ == '__main__': cli()
