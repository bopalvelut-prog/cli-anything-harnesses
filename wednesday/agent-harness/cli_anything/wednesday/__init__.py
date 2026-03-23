import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('wednesday running')
@cli.command()
def start(): click.echo('wednesday started')
if __name__ == '__main__': cli()
