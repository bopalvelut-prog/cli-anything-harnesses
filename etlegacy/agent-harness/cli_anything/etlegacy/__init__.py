import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('etlegacy running')
@cli.command()
def start(): click.echo('etlegacy started')
if __name__ == '__main__': cli()
