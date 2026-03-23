import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('navigator running')
@cli.command()
def start(): click.echo('navigator started')
if __name__ == '__main__': cli()
