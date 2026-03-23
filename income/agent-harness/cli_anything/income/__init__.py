import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('income running')
@cli.command()
def start(): click.echo('income started')
if __name__ == '__main__': cli()
