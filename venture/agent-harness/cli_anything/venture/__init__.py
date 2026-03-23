import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('venture running')
@cli.command()
def start(): click.echo('venture started')
if __name__ == '__main__': cli()
