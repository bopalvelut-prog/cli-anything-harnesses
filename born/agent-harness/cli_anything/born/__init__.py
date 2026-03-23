import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('born running')
@cli.command()
def start(): click.echo('born started')
if __name__ == '__main__': cli()
