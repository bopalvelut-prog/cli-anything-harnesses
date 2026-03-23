import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('countly running')
@cli.command()
def start(): click.echo('countly started')
if __name__ == '__main__': cli()
