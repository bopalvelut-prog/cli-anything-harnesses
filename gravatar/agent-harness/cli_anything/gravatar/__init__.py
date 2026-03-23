import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('gravatar running')
@cli.command()
def start(): click.echo('gravatar started')
if __name__ == '__main__': cli()
