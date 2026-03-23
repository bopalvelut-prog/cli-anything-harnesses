import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('zap running')
@cli.command()
def start(): click.echo('zap started')
if __name__ == '__main__': cli()
