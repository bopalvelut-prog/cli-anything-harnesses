import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('fever running')
@cli.command()
def start(): click.echo('fever started')
if __name__ == '__main__': cli()
