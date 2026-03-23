import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('authentic running')
@cli.command()
def start(): click.echo('authentic started')
if __name__ == '__main__': cli()
