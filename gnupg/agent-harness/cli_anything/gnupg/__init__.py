import click
@click.group()
def cli(): pass
@cli.command()
def status(): click.echo('gnupg running')
@cli.command()
def start(): click.echo('gnupg started')
if __name__ == '__main__': cli()
