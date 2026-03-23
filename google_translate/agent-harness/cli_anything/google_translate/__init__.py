import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('google_translate running')
@cli.command()
def start(): click.echo('google_translate started')
if __name__ == '__main__': cli()
