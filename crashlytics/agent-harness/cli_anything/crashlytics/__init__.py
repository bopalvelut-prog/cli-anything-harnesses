import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('crashlytics running')
@cli.command()
def start(): click.echo('crashlytics started')
if __name__ == '__main__': cli()
