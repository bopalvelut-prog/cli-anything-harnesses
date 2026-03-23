import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('lay running')
@cli.command()
def start(): click.echo('lay started')
if __name__ == '__main__': cli()
