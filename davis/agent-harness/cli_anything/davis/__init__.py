import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('davis running')
@cli.command()
def start(): click.echo('davis started')
if __name__ == '__main__': cli()
