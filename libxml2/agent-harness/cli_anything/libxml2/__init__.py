import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('libxml2 running')
@cli.command()
def start(): click.echo('libxml2 started')
if __name__ == '__main__': cli()
