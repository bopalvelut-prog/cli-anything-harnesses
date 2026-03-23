import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('resolution running')
@cli.command()
def start(): click.echo('resolution started')
if __name__ == '__main__': cli()
