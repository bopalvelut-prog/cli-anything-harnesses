import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('ats running')
@cli.command()
def start(): click.echo('ats started')
if __name__ == '__main__': cli()
