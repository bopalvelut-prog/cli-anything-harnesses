import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('live running')
@cli.command()
def start(): click.echo('live started')
if __name__ == '__main__': cli()
