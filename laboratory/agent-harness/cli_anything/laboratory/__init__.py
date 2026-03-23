import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('laboratory running')
@cli.command()
def start(): click.echo('laboratory started')
if __name__ == '__main__': cli()
