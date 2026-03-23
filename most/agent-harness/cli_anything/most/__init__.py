import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('most running')
@cli.command()
def start(): click.echo('most started')
if __name__ == '__main__': cli()
