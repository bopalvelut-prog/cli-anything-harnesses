import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('burst running')
@cli.command()
def start(): click.echo('burst started')
if __name__ == '__main__': cli()
