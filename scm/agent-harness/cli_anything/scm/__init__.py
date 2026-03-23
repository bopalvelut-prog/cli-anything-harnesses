import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('scm running')
@cli.command()
def start(): click.echo('scm started')
if __name__ == '__main__': cli()
