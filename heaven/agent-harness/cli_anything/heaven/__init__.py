import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('heaven running')
@cli.command()
def start(): click.echo('heaven started')
if __name__ == '__main__': cli()
